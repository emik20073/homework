class TooManyStudentsError(Exception):
    def __init__(self, message="too many students in the group"):
        super().__init__(message)

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name


    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book


    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, record book:{self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise TooManyStudentsError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        students = '\n'.join(str(student) for student in self.group)
        return f'Group {self.number}:\n{students}'
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

try:
    for i in range(9):  # ще 9 студентів
        gr.add_student(Student('Male', 20 + i, f'Name{i}', f'Last{i}', f'ID{i}'))

    # 11-й студент викличе виняток
    gr.add_student(Student('Female', 22, 'Anna', 'Ivanova', 'ID999'))

except TooManyStudentsError as e:
    print(f'error: {e}')