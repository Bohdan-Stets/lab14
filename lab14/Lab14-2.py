class Student:
    def __init__(self, name, specialty, course):
        self.name = name
        self.specialty = specialty
        self.course = course

    def calculate_group_number(self):
        return f"Група {self.specialty}-{self.course}"

    def __str__(self):
        return f"Студент {self.name}, Спеціальність: {self.specialty}, Курс: {self.course}"

class StudentIntern(Student):
    def __init__(self, name, specialty, course, practice_institution):
        super().__init__(name, specialty, course)
        self.practice_institution = practice_institution

    def calculate_group_number(self):
        return "Ви тимчасово переводитесь у Групу 40"

    def __str__(self):
        return (f"Студент-практикант {self.name}, Спеціальність: {self.specialty},"
                f"Курс: {self.course}, Заклад практики: {self.practice_institution}")

name = input("Введіть ім'я студента: ")
specialty = input("Введіть спеціальність студента: ")
course = int(input("Введіть курс студента: "))

student1 = Student(name, specialty, course)
print(student1)
print(student1.calculate_group_number())

practice_institution = input("Введіть заклад практики: ")

intern1 = StudentIntern(name, specialty, course, practice_institution)
print(intern1)
print(intern1.calculate_group_number())
