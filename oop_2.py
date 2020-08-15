# we must need to initialize the argument value of a class
# in any method of class we need to initialize that with self keyword
# Either a value or None
# without the initialization it will give a runtime error


class ListOfItem:
    __name = "Jubair"

    def __init__(self, items=list()):  # example of passing a list as a argument in methode
        self.__items = items

    def add_item(self, i: str):
        self.__items.append(i)

    def show_items(self):
        return self.__items

    def get_name(self):
        return self.__name


fruits = ["Banana", "Apple", "Mango", "Pine-Apple", "Watermelon"]

item = ListOfItem(fruits)
print(item.show_items())
item.add_item("Lychee")
print(item.show_items())
print(item.get_name())
