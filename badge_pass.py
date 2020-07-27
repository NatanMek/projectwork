import random
import datetime
date_format = "%d/%m/%Y %H:%M:%S"

Name = []
Surname = []
Tax_code = []
Badge_number = []
Presence = []


def newbadge():

    name = input("Nome: ")
    Name.append(name)
    surname = input("Surname: ")
    Surname.append(surname)
    tax_code = input("C.F: ")
    Tax_code.append(tax_code)
    Presence.append(False)
    date = datetime.datetime.now().strftime(date_format)
    Badge_number.append(random.randint(1, 100))
    print(f'This is your data:\n Name:{Name[-1]}\n Surname:{Surname[-1]}\n Tax Code:{Tax_code[-1]}\n Badge_number:{Badge_number[-1]}')


def access():

    number = int(input("Insert your Badge number: "))
    cont = 0
    for i in range(len(Badge_number)):
        if number == Badge_number[i]:
            cont = cont + 1
            Presence[i] = True
    if cont > 0:
        print(f"Welcome {Name[-1]}!")
    else:
        print("The Badge number you've inserted is incorrect")


def exit():

    number = int(input("Insert your Badge number: "))
    cont = 0
    for i in range(len(Badge_number)):
        if number == Badge_number[i]:
            cont = cont + 1
            Presence[i] = False
    if cont > 0:
        print(f"Goodbye {Name[-1]}!")
    else:
        print("The Badge number you've inserted is incorrect")


while True:

    print("1: Access\n2: Exit\n3: Create new User")
    choice = int(input("> "))
    if 0 < choice < 4:
        if choice == 1:
            access()
        if choice == 2:
            exit()
            break
        if choice == 3:
            newbadge()