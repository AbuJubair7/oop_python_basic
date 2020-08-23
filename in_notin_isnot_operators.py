# given example of in/not in / is not operators
# 'in', 'not in' operator is basically used for a find a value from a list/string
# 'is not' operator only used for no literal object like 'None'

grocery = ["Mango", "Apple", "Banana"]

if "Mango" in grocery:
    print(True)
else:
    print(False)

if "Juice" not in grocery:
    print(True)
else:
    print(False)

name = "Juabir"

if "J" in name:
    print(True)
else:
    print(False)

print("c" in name)

flag = True if 3 > 4 else False  # ternary operator
print(flag)

s = None
print("True" if s is not None else False)  # similar with print("True" if s != None else False)

