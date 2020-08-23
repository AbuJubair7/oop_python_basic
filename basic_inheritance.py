# python supports multiple inheritance
# also need to call super class init method inside child class init
# there is also a example of method overriding
# here is a pre defined method called __str__() which is used to show object information like get_summary
# in order to get the data we just need to call object.__str__(pass object variable here)

class Person:

    def __init__(self, name, age: int, dob: str, address: str, mobile_number: str):
        self.__name = name
        self.__age = age
        self.__dob = dob
        self.__address = address
        self.__mobile_number = mobile_number

    def set_name(self, name: str):
        self.__name = name

    def set_age(self, age: int):
        self.__age = age

    def set_dob(self, dob: str):
        self.__dob = dob

    def set_address(self, address: str):
        self.__address = address

    def set_mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_dob(self):
        return self.__dob

    def get_address(self):
        return self.__address

    def get_mobile_number(self):
        return self.__mobile_number

    def get_summary(self):
        return f"Name : {self.get_name()}\nAge : {self.get_age()}\nDOB : {self.get_dob()}\nAddress : {self.get_address()}" \
               f"\nMobile number : {self.get_mobile_number()}"


class Student(Person):
    def __init__(self, name, age: int, dob: str, address: str, mobile_number: str, student_id: str):
        super().__init__(name, age, dob, address, mobile_number)
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    # override method
    def get_summary(self):
        return f"Name : {self.get_name()}\nAge : {self.get_age()}\nDOB : {self.get_dob()}\nAddress : {self.get_address()}" \
               f"\nMobile number : {self.get_mobile_number()}\nStudent id : {self.get_student_id()}"

    def __str__(self):
        return f"Name : {self.get_name()}\nAge : {self.get_age()}\nDOB : {self.get_dob()}\nAddress : {self.get_address()}" \
               f"\nMobile number : {self.get_mobile_number()}\nStudent id : {self.get_student_id()}"


s1 = Student("Maisha", 18, "6 September 2002", "new Railway Station, Kurigram", "01907468301", "2121")
print(s1.get_summary())
print(s1)
