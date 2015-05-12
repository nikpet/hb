import sqlite3
from Client import Client
import re
from hashlib import sha1

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT
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
        SELECT id, username, balance, message
        FROM clients
        WHERE username = ? AND password = ?
        LIMIT 1
    """
    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False


def log_failed_login(username):
    update_sql = """
        UPDATE clients
        (login_attempts, last_login_attempt)
        VALUES (login_attempts + 1, date(now))
    """
    cursor.execute(update_sql)
    conn.commit
