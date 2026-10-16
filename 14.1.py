class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name},{self.last_name}, {self.gender},{self.age}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender,age,first_name,last_name)
        self.record_book = record_book


class Group:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def  delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.students.remove(student)

    def __str__(self):
        return "\n".join([str(student) for student in self.students])

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group()
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print((gr.find_student('Jobs')))
print(gr.find_student('Jobs2'))
print(isinstance(gr.find_student('Jobs'), Student))

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
