#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#
class Person():
    def __init__(self, name):
        self.name = name

    def enrol_detail(self, gender, age):
        self.gender = gender
        self.age = age

        if (gender != None) & (age != None):
            call = ''
            match gender:
                case 'female':
                    call = 'Miss'
                case 'male':
                    call = 'Mr'
                case _:
                    call = self.name
            print(f"Hi, {call}, nice to meet you, here is your info:")
            print(f"name: {self.name}, gender: {self.gender}, age: {self.age}")
        else:
            print('Error: please complete your info')


class Student(Person):
    def __init__(self, grade):
        super().__init__('Person')
        self.grade = grade
        print('welcome to grade', grade)

    def enrol_detail(self, gender, age):
        super().enrol_detail(gender, age)


person1 = Person('Mia')
person1.enrol_detail('female', 12)

stu1 = Student('seven')
stu1.enrol_detail('male', 7)
