class Human:
    def __init__(self,name,age,favorite_lesson):
        self.name =name
        self.age = age
        self.favorite_lesson = favorite_lesson
    def __str__(self):
        return f'{self.name}, {self.age}, {self.favorite_lesson}'


class Teacher(Human):
    def __init__(self,specciality,salary):
        self.specciality = specciality
        self.salary = salary
    def __str__(self):
        return f'{self.specciality}, {self.salary}'

class Student(Human):
    def __init__(self,grade):
        self.grade = grade

    def __str__(self):
        return f'{self.grade}'

Nurlan = Human ('Nuraln',18,'well')
Artur = Teacher ('mathematician',10.000)
Alina = Student (5)

print ( Alina )


