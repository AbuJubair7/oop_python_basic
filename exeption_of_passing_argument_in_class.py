class ArgumentTest:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

    def add_obj(self, obj):
        obj.show_name()


# we cannot declare argument type or a default argument of that existing classs
# this will not compile
# example showed below
#  def add_obj(self, obj:ArgumentTest):
#      obj.show_name()
#
#  def add_obj(self, obj:ArgumentTest = ArgumentTest("X")):
#      obj.show_name()


# but we can declare another argument type or default argument of another class in other class method
# example showed below
class Test:
    def __init__(self):
        None

    def add_another_obj(self, ob1=ArgumentTest("test name")):
        ob1.show_name()

    def show_obj_name(self, ob2: ArgumentTest):
        ob2.show_name()


obj1 = ArgumentTest("Jubair")
obj1.show_name()
obj2 = ArgumentTest("Test")
obj1.add_obj(obj2)

test = Test()
test.add_another_obj()  # this will show a default object name because there is no argument passed
test.show_obj_name(obj1)  # here passing argument except ArgumentTest object will show error
