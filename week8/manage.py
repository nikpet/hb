import sqlite3


class Manage:
    def __init__(self):
        self.db = sqlite3.connect('hr.db')
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.run()

    def list_students(self):
        query = """
                SELECT name, github
                FROM students
                """
        students = self.cursor.execute(query).fetchall()
        for student in students:
            print (student['name'], student['github'], sep=' - ')

    def list_courses(self):
        query = """
                SELECT name
                FROM courses
                """
        courses = self.cursor.execute(query).fetchall()
        for course in courses:
            print(course['name'])

    def get_students_courses(self):
        query = """
                SELECT students.name as student, courses.name as course
                FROM students
                JOIN students_to_courses ON students.id = student_id
                JOIN courses ON course_id = courses.id
                """
        result = dict()
        students_courses = self.cursor.execute(query)
        for student_course in students_courses:
            if student_course[0] not in result:
                result[student_course[0]] = [student_course[1]]
            else:
                result[student_course[0]].append(student_course[1])
        return result

    def list_students_courses(self):
        print(self.get_students_courses())

    def list_students_with_most_courses(self):
        query = """
                SELECT name, COUNT(student_id) as cnt FROM students
                JOIN students_to_courses ON students.id = student_id
                GROUP BY name
                ORDER BY cnt DESC
                """
        rowset = self.cursor.execute(query).fetchall()
        max_number = rowset[0]['cnt']
        for row in rowset:
            if max_number > row['cnt']:
                break
            print(row['name'], row['cnt'])


    def run(self):
        while True:
            command = input('command>').lower()
            if command in ['q', 'quit']:
                break
            elif command in ['ls', 'list students']:
                self.list_students()
            elif command in ['lc', 'list courses']:
                self.list_courses()
            elif command in ['lsc', 'list students courses']:
                self.list_students_courses()
            elif command in ['m', 'most courses']:
                self.list_students_with_most_courses()
            else:
                print("Invalid command")


if __name__ == '__main__':
    m = Manage()
