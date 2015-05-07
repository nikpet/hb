import requests
import sqlite3
import json


class Hr:
    def __init__(self):
        self.db = sqlite3.connect('hr.db')
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.api_uri = 'https://hackbulgaria.com/api/students/'
        self._init_db()

    def _init_db(self):
        create_students_table = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            github TEXT,
            available INTEGER
            )
            """
        create_courses_table = """
            CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
            """
        create_students_to_courses_table = """
            CREATE TABLE IF NOT EXISTS students_to_courses (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            `group` INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id)
            FOREIGN KEY(course_id) REFERENCES courses(id)
            )
        """

        self.cursor.execute(create_students_table)
        self.cursor.execute(create_courses_table)
        self.cursor.execute(create_students_to_courses_table)

    def create_student(self, data):
        query = """
            INSERT INTO students
            (name, github, available)
            VALUES (:name, :github, :available)
            """
        self.cursor.execute(query, data)
        return self.cursor.lastrowid

    def create_course(self, data):
        query = """
            INSERT INTO courses (name) VALUES (:name)
            """
        self.cursor.execute(query, data)
        return self.cursor.lastrowid

    def create_relation(self, data):
        query = """
            INSERT INTO students_to_courses
            (student_id, course_id, `group`)
            VALUES (:student_id, :course_id, :group)
            """
        self.cursor.execute(query, data)
        return self.cursor.lastrowid

    def get_or_create_course_id(self, name):
        query = 'SELECT id FROM courses WHERE name = :name'
        course_id = self.cursor.execute(query, name).fetchone()
        if course_id is None:
            course_id = self.create_course(name)
        else:
            course_id = course_id[0]
        return course_id

    def get_or_create_student_id(self, data):
        query = 'SELECT id FROM courses WHERE name = :name'
        student_id = self.cursor.execute(query, data).fetchone()
        if student_id is None:
            student_id = self.create_student(data)
        else:
            student_id = student_id[0]
        return student_id

    def api2db(self):
        # SWAP for using requests
        # data = requests.get(self.api_uri).json()
        with open('students.json') as fd:
            data = json.load(fd)
        fd.close()
        for student in data:
            student_id = self.get_or_create_student_id(student)
            for course in student['courses']:
                course_id = self.get_or_create_course_id(course)
                self.create_relation({'student_id': student_id,
                                      'course_id': course_id,
                                      'group': course['group']})
        self.db.commit()
        self.db.close()

if __name__ == '__main__':
    hr = Hr()
    print(hr.api2db())
