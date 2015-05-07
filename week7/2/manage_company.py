import sqlite3


class ManageCompany:
    def __init__(self):
        self.db = sqlite3.connect("company.db")
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.help_commands = {
            'quit': 'Exit program',
            'list_employees': 'List employees (name - possition)',
            'monthly_spending': 'Company mounthly spendings',
            'yearly_spending': 'Company yearly spendings',
            'add_employee': 'Add employee',
            'delete_employee <id>': 'Delete employee',
            'update_employee <id>': 'Update employee'
            }
        self.available_commands = {
            'quit': 0,
            'list_employees': 0,
            'monthly_spending': 0,
            'yearly_spending': 0,
            'add_employee': 0,
            'delete_employee': 1,
            'update_employee': 1,
            'q': 0, 'le': 0, 'ms': 0, 'ys': 0, 'ae': 0, 'de': 1, 'ee': 1
            }
        self.start()

    def ask_for_command(self, prompt="command>"):
        return input(prompt).lower()

    # Just a short cut
    def le(self):
        return self.list_employees()

    def list_employees(self):
        query = "SELECT id, name, position FROM employees"
        result = self.cursor.execute(query).fetchall()
        formated_result = []
        for employee in result:
            formated_result.append(' - '.join([str(x) for x in employee]))
        return formated_result

    def _get_monthly_spendings(self):
        query = "SELECT SUM(monthly_salary) FROM employees"
        return self.cursor.execute(query).fetchone()[0]

    # Just a short cut
    def ms(self):
        return self.monthly_spending()

    def monthly_spending(self):
        return "The company is spending {} every month!".format(
            self._get_monthly_spendings()
            )

    def _get_yearly_spending(self):
        query = "SELECT SUM(yearly_bonus) FROM employees"
        early_bonuses = self.cursor.execute(query).fetchone()[0]
        return self._get_monthly_spendings() * 12 + early_bonuses

    def _is_sure(self, question):
        question += ' [y/N]'
        answer = self.ask_for_command(question)
        if answer == '' or answer == 'n':
            return False
        elif answer == 'y':
            return True
        else:
            self._is_sure(question)

    # Just a short cut
    def ys(self):
        return self.yearly_spending()

    def yearly_spending(self):
        return "The company is spending {} every year!".format(
            self._get_yearly_spending()
            )

    # Just a short cut
    def ae(self):
        return self.add_employee()

    def add_employee(self):
        name = self.ask_for_command('name>')
        while len(name) < 5:
            print("Name must be longer than 5 characters")
            name = self.ask_for_command('name>')
        salary = int(self.ask_for_command('monthly_salary>'))
        while salary <= 0:
            print("We don't allow slavery in our company(sallary must be > 0)")
            salary = int(self.ask_for_command('monthly_salary>'))
        bonus = int(self.ask_for_command('yearly_bonus>'))
        while bonus < 0:
            print("You can't steal from our employees (yearly_bonus >= 0)")
            bonus = int(self.ask_for_command('yearly_bonus>'))
        position = self.ask_for_command('position>')
        while len(position) < 2:
            print("Position must be longer than 2 characters")
            position = self.ask_for_command('position>')
        query = "INSERT INTO employees VALUES(?,?,?,?,?)"
        self.cursor.execute(query, (None, name, salary, bonus, position))
        return "Employee added"

    # Just a short cut
    def de(self, employee_id):
        return self.delete_employee(employee_id)

    def delete_employee(self, employee_id):
        select_query = "SELECT name FROM employees WHERE id = ?"
        try:
            name = self.cursor.execute(select_query, employee_id).fetchone()[0]
        except Exception:
            return "No such employee id"
        delete_query = "DELETE FROM employees WHERE id = ?"
        question = "Are you sure you want to delete {}".format(name)
        if self._is_sure(question):
            self.cursor.execute(delete_query)
            return name + " was deleted"

    # Just a short cut
    def ee(self, employee_id):
        return self.edit_employee(employee_id)

    def edit_employee(self, employee_id):
        select_query = """SELECT name, monthly_salary, yearly_bonus, position
        FROM employees WHERE id = ?"""
        try:
            employee = self.cursor.execute(select_query, employee_id).fetchone()
        except Exception:
            return "No such employee id"
        update_query = "UPDATE employees SET {}, WHERE id=?"
        changed = []
        query_updates = {
            'name': 'name = ?',
            'sallary': 'monthly_salary = ?',
            'bonus': 'yearly_bonus = ?',
            'position': 'position = ?'
            }
        prompt = 'name[{}]>'.format(employee['name'])
        name = self.ask_for_command(prompt)
        while len(name) < 5:
            if name == '':
                name = employee['name']
                break
            else:
                changed.append('name')
            print("Name must be longer than 5 characters")
            name = self.ask_for_command(prompt)
        prompt = 'monthly_salary[{}]>'.format(employee['monthly_salary'])
        salary = self.ask_for_command(prompt)
        if salary == '':
            salary = employee['monthly_salary']
        else:
            salary = int(salary)
        while salary <= 0:
            if salary == '':
                salary = employee['monthly_salary']
                break
            else:
                changed.append('salary')
            print("We don't allow slavery in our company(sallary must be > 0)")
            salary = int(self.ask_for_command(prompt))
        prompt = 'yearly_bonus[{}]>'.format(employee['yearly_bonus'])
        bonus = self.ask_for_command(prompt)
        if bonus == '':
            bonus = employee['yearly_bonus']
        else:
            bonus = int(bonus)
            changed.append('bonus')
        while bonus < 0:
            if bonus == '':
                bonus = employee['yearly_bonus']
                break
            else:
                changed.append('bonus')
            print("You can't steal from our employees (yearly_bonus >= 0)")
            bonus = int(self.ask_for_command(prompt))
        prompt = 'position[{}]>'.format(employee['position'])
        position = self.ask_for_command(prompt)
        while len(position) < 2:
            if position == '':
                position = employee['position']
                break
            else:
                changed.append('position')
            print("Position must be longer than 2 characters")
            position = self.ask_for_command(prompt)
        print(changed)
        if len(changed) > 0:
            update_query.format(', '.join([query_updates[x] for x in changed]))
            return update_query
        else:
            return None

    def execute(self, command_with_arg):
        command, arg = command_with_arg
        if arg is not None and self.available_commands[command] != 0:
            result = getattr(self, command)(arg)
        else:
            result = getattr(self, command)()
        if result is None:
            return None
        if type(result) is list or type(result) is tuple:
            for row in result:
                print(row)
        else:
            print(result)

    def start(self):
        while True:
            command_with_arg = self.ask_for_command()
            if ' ' in command_with_arg:
                command = command_with_arg.split(' ', 1)
            else:
                command = [command_with_arg, None]
            if command[0] not in self.available_commands:
                print("Ivalid command use help or ? for available commands")
            elif command[0] == "quit" or command[0] == "q":
                break
            else:
                # self.execute(command)
                try:
                    self.execute(command)
                except TypeError:
                    print("Missing second argument for {}".format(command[0]))
        self.db.commit()
        self.db.close()


if __name__ == '__main__':
    mc = ManageCompany()
