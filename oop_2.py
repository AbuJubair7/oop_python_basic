# we must need to initialize the argument value of a class
# in any method of class we need to initialize that with self keyword
# Either a value or None
# without the initialization it will give a runtime error
# Showed example of static variable and method


class ListOfItem:
    name = "Jubair"  # static member variable

    def __init__(self, items=list()):  # example of passing a list as a argument in methode
        self.__items = items

    def add_item(self, i: str):
        self.__items.append(i)

    def show_items(self):
        return self.__items

    # static method
    @staticmethod
    def show_info():
        return "Hi ! This is python."


fruits = ["Banana", "Apple", "Mango", "Pine-Apple", "Watermelon"]

item = ListOfItem(fruits)
print(item.show_items())
item.add_item("Lychee")
print(item.show_items())

# another way of calling method from class but there need to pass class object as 'self' parameter
print(ListOfItem.show_items(item))

# calling static variable and method
print(ListOfItem.name)
print(ListOfItem.show_info())


