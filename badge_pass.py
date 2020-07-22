def badge():
    name = "Natan"
    surname = "Mek"
    cf = "MKNNTN93R28F205I"


a = 3
b = 5

admitted = ["Luca", "Stefano", "Natan"]
print(len(admitted))
print(admitted)


def setnew():
    new = input("New Employee: ")
    admitted.append(new)


new_list = input("New Employee: ")

admitted.append(new_list)
print(admitted)
i = 0

name_info = input("What's your name?:  ")
for v in admitted:
    if name_info == v:
        print(v, "Access Granted!")
    else:
        print(v, "Access not granted! Wait for your turn...")
