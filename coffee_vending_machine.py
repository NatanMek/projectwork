class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class VendingMachine:

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

        self.money_inserted = 0.00

    def display_items(self):
        for code, item in enumerate(self.items, start=1):
            print(f"[{code}] - {item.name} (€{item.price:.2f})")

    def insert_money(self, money):
        if money <= 0.00:
            raise ValueError
        self.money_inserted += money


def switch(choice):
    switcher = {
        1: "Preparing High Quality coffee beans..."
           "Brewing coffee..."
           "Caffè is served",
        2: "Making Cappucino..."
           "Steaming the milk..."
           "Frothing the milk..."
           "Making espresso..." 
           "Adding the milk to the espresso..."
           "Cappuccino is served",
        3: "Making milk..."
           "Making espresso..."
           "Steaming the milk..."
           "Adding the milk to the espresso..."
           "Macchiato is served",
        4: "Making 40 ml of coffee..."
           "Caffè lungo is served",
        5: "Making 20 ml of coffee..."
           "Caffè Ristretto is served",
        6: "Making Latte..."
           "Adding 20 ml of coffee to Latte..."
           "Latte macchiato is ready",
        7: "Making espresso..."
           "Adding 70 ml of water"
           "Americano is served",
        8: "Making Espresso..."
           "Preparing microfoam of milk..."
           "Adding microfoam to the espresso..."
           "Flat White is served",
    }
    print(switcher.get(choice, "Invalid item"))


def main():

    vending_machine = VendingMachine()
    vending_machine.display_items()

    while True:
        try:
            user_selection = int(input("Please enter the desired item code: "))
            if user_selection not in vending_machine.items:
                print("Invalid item code, please try again...")
        except ValueError:
            continue
        if user_selection in range(1, len(vending_machine.items)+1):
            break
    item = vending_machine.items[user_selection-1]
    print(f"You've selected \"{item.name}\" - the price is €{item.price:.2f}")
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
    print(f"Thank you! Please take your \"{item.name}\".")
    print(f"The remaining change in the machine is €{vending_machine.money_inserted - item.price:.2f}.")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
