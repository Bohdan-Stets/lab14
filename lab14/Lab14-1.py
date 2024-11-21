class Worker:
    def __init__(self, last_name, salary):
        self.last_name = last_name
        self.salary = salary

    def calculate_tax(self):
        if self.salary <= 1100:
            return 0
        elif self.salary <= 4000:
            return self.salary * 0.10
        else:
            return self.salary * 0.20

    def __str__(self):
        return f"Робітник {self.last_name}, Зарплата: {self.salary} грн, Податок: {self.calculate_tax()} грн"

last_name = input("Введіть прізвище робітника: ")
salary = float(input("Введіть заробітну плату робітника: "))

worker1 = Worker(last_name, salary)
print(worker1)
