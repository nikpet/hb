import sqlite3
from Client import Client
import re
from hashlib import sha1

conn = sqlite3.connect("bank.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                login_attempts INT DEFAULT 0,
                last_login_attempt DATETIME DEFAULT current_timestamp
                )'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = """
        UPDATE clients
        SET message = ?
        WHERE id = ?
    """
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def is_strong(password):
    if len(password) < 8:
        return False
    if not re.search('[a-z]', password):
        return False
    if not re.search('[A-Z]', password):
        return False
    if not re.search('[0-9]', password):
        return False
    if not re.search("""[\~\`\!\@\#\$\%\^\&\*\(\)\_\-\+\=\{
            \}\[\]\:\;\"\'\\\?\/\>\<\,\.]""", password):
        return False
    return True


def hash_pass(password):
    return sha1(password.encode())


def change_pass(new_pass, logged_user):
    update_sql = """
        UPDATE clients
        SET password = ?
        WHERE id = ?
    """
    if is_strong(new_pass):
        cursor.execute(update_sql, (new_pass, logged_user.get_id()))
        conn.commit()
        return True
    else:
        return False


def register(username, password):
    insert_sql = """
        INSERT INTO clients (username, password)
        VALUES (?, ?)
    """
    if is_strong(password):
        cursor.execute(insert_sql, (username, password))
        conn.commit()
        return True
    else:
        return False


def login(username, password):
    select_query = """
        SELECT id, username, balance, message, login_attempts,
        last_login_attempt
        FROM clients
        WHERE username = ? AND password = ?
        LIMIT 1
    """
    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user['id'], user['username'], user['balance'],
                      user['message'])
    else:
        log_failed_login(username)
        return False


def reset_failed_login(username):
    update_sql = """
        UPDATE clients
        SET login_attempts = 0
        WHERE username = ?
    """
    cursor.execute(update_sql, username)
    conn.commit()


def log_failed_login(username):
    update_sql = """
        UPDATE clients
        SET login_attempts = login_attempts + 1,
            last_login_attempt = datetime('now')
        WHERE username = ?
        """
    cursor.execute(update_sql, (username, ))
    conn.commit()
