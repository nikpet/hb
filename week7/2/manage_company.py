import sqlite3


class ManageCompany:

    def __init__(self):
        self.db = sqlite3.connect("company.db")
        self.cursor = self.db.cursor()
        self.start()

    def __init_db(self, drop=False, populate=False):
        if drop:
            print('Table will be reCreated')
            self.cursor.execute("DROP TABLE IF EXISTS employees")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, monthly_sallary INTEGER, yearly_bonus INTEGER,
        possition)""")

        if populate:
            values = [(1, "Ivan Ivanov", 5000, 1000, "Software Developer"),
                      (2, "Rado Rado", 5000, 1000, "Technical Support Intern"),
                      (3, "Ivo Ivo", 5000, 1000, "CEO"),
                      (4, "Petar Petrov", 5000, 1000, "Marketing Manager"),
                      (5, "Maria Georgieva", 5000, 1000, "COO")]
            self.cursor.executemany("INSERT INTO employees VALUES(?,?,?,?,?)",
                                    values)
            self.db.commit()

    def start(self):
        self.__init_db()
        while True:
            command = self.get_command('command>').lower()
            if command == 'list_employees':
                self.list_employees()
            if command == 'monthly_spending':
                break
            if command == 'yearly_spending':
                break
            if command == 'add_employee':
                break
            if command[:15] == 'delete_employee':
                break
            if command[:15] == 'update_employee':
                break
            if command == 'quit':
                break
            if command == 'recreate':
                if self.is_warned('Are you sure this will delete current table'):
                    self.__init_db(drop=True)
                else:
                    print("Database not recreated")
            if command == 'populate':
                if self.is_warned('Are you sure, any data already inserted will be lost'):
                    self.__init_db(drop=True, populate=True)
                else:
                    print("Database not populated")

    def is_warned(self, text):
        answer = self.get_command(text + ' [y/N]>')
        if answer == 'y':
            return True
        elif answer == 'n' or answer == '':
            return False
        else:
            self.is_warned(text)

    def list_employees(self):
        print(self.cursor.execute('SELECT * FROM employees').fetchall())

    def get_command(self, prompt='command>'):
        return input(prompt).lower()


if __name__ == '__main__':
    mc = ManageCompany()
