
from student import Student


class Group:
    def __init__(self, number):
        self.number = number
        self.students = set()


    def add_student(self, student):
        self.students.add(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.students.remove(student)

    def __str__(self):
        students_list = '\n'.join(
            str(student) for student in sorted(
                self.students, key=lambda student: str(student)
            )
        )
        return f'Group {self.number}:\n{students_list}'
