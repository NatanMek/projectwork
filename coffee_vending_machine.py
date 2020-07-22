import sys
import time


class Item:  # define class Item with  2 parameters (name, price)

    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:  # define VendingMachine class and initialize with all the vending machine items

    def __init__(self):

        self.items = [
            Item("Caffè", 0.30),
            Item("Cappuccino", 0.90),
            Item("Macchiato", 1.00),
            Item("Caffè lungo", 0.80),
            Item("Caffè Ristretto", 0.60),
            Item("Latte macchiato", 1.50),
            Item("Americano", 1.80),
            Item("Flat White", 2.00)
        ]

        self.money_inserted = 0.00  # initialize the money available in the vending machine

    def display_items(self):  # function to display the items with their price
        print("##################################")
        print(" Welcome to Natan's CVM(Coffee Vending Machine) ")
        for code, item in enumerate(self.items, start=1):
            print(f"[{code}] - {item.name} (€{item.price:.2f})")
        print("##################################")

    def insert_money(self, money):  # function for money insert
        if money <= 0.00:
            raise ValueError
        self.money_inserted += money


def update(total, progress):

    bar_length, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(bar_length * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "#" * block + "-" * (bar_length - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()


runs = 30


def main():
    vending_machine = VendingMachine()
    vending_machine.display_items()

    def switch(choice):  # switch function in order to display preparation of the item
        switcher = {
            1: "Preparing High Quality coffee beans..."
               "Brewing coffee...",
            2: "Making Cappucino..."
               "Steaming the milk..."
               "Frothing the milk..."
               "Making espresso..."
               "Adding the milk to the espresso...",
            3: "Making milk..."
               "Making espresso..."
               "Steaming the milk..."
               "Adding the milk to the espresso...",
            4: "Making 40 ml of coffee...",
            5: "Making 20 ml of coffee...",
            6: "Making Latte..."
               "Adding 20 ml of coffee to Latte...",
            7: "Making espresso..."
               "Adding 70 ml of water...",
            8: "Making Espresso..."
               "Preparing microfoam of milk..."
               "Adding microfoam to the espresso...",
        }
        print(switcher.get(choice, "Invalid item"))

    def key_card(credit):
        while True:
            try:
                selected = int(input("Please enter the desired item code: "))
                if selected not in range(1, len(vending_machine.items) + 1):
                    print("Invalid item code, please try again...")
            except ValueError:
                continue
            if selected in range(1, len(vending_machine.items) + 1):
                break
        item = vending_machine.items[selected - 1]
        print(f"You've selected \"{item.name}\" - the price is €{item.price:.2f}")
        print("Sugar: 1-Less, 2-Medium, 3-Maximum")
        sugar_choice = input("Please choose sugar quantity: ")
        if sugar_choice == '1':
            print("You choose less quantity of sugar")
        elif sugar_choice == '2':
            print("You choose medium quantity of sugar")
        elif sugar_choice == '3':
            print("You choose maximum quantity of sugar")
        else:
            print("Please choose a valid sugar quantity...")

        if credit - item.price < 0:
            print(f"You're key card has not sufficient credit!")
            while True:
                credit_to_insert = float(
                    input(f"You need to insert €{abs(credit - item.price): .2f} in order to continue: "))
                credit = credit_to_insert + credit
                if credit >= item.price:
                    print("Well done! Let's continue..")
                    break
        else:
            print(f"You're key card has €{credit:.2f}.")
        remaining_money_key = credit - item.price
        switch(selected)
        for run_num in range(runs):
            time.sleep(.1)
            update(runs, run_num + 1)
        print(f"Thank you! Please take your \"{item.name}\".")
        print(f"The remaining change in your key card is €{remaining_money_key:.2f}.")
        print("Have a nice day!")

        return 0

    while True:
        try:
            type_of_payment = str(input("Do you have a key card? "))
            if type_of_payment == 'yes':
                key_card(0.50)
                exit(1)
            else:
                user_selection = int(input("Please enter the desired item code: "))
            if user_selection not in range(1, len(vending_machine.items) + 1):
                print("Invalid item code, please try again...")
        except ValueError:
            continue
        if user_selection in range(1, len(vending_machine.items) + 1):
            break
    item = vending_machine.items[user_selection - 1]
    print(f"You've selected \"{item.name}\" - the price is €{item.price:.2f}")
    print("Sugar: 1-Less, 2-Medium, 3-Maximum")
    sugar_choice = input("Please choose sugar quantity: ")
    if sugar_choice == '1':
        print("You choose less quantity of sugar")
    elif sugar_choice == '2':
        print("You choose medium quantity of sugar")
    elif sugar_choice == '3':
        print("You choose maximum quantity of sugar")
    while vending_machine.money_inserted < item.price:
        print(f"You've inserted €{vending_machine.money_inserted:.2f} into the machine so far.")
        while True:
            try:
                money_to_insert = float(input("Please enter the amount of money you'd like to insert: "))
                vending_machine.insert_money(money_to_insert)
            except ValueError:
                continue
            else:
                break
    switch(user_selection)
    for run_num in range(runs):
        time.sleep(.1)
        update(runs, run_num + 1)
    print(f"Thank you! Please take your \"{item.name}\".")
    print(f"The remaining change in the machine is €{vending_machine.money_inserted - item.price:.2f}.")
    print("Have a nice day!")

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
