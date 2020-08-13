# cannot define multiple __init__() methode in Python
# __ before any methode or arguments is stand for private access modifier

class Person:

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def view_summary(self):
        return f"Name :{self.__name if self.__name is not None else 'Invalid'}\nAge :{self.__age if self.__age is not None else 'Invalid'}"


p1 = Person("P1", 22)
p2 = Person("P2", 24)
p3 = Person("P3", 12)
p4 = Person("P4", 11)
p5 = Person("P5", 25)
p6 = Person("P6", 26)
p7 = Person("P7", 26)

persons = [p1, p2, p3, p4, p5, p6, p7]

for person in persons:
    print(f"{person.view_summary()}\n")
