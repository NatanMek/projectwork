import sqlite3
import random
import datetime
import matplotlib.pyplot as plt


# Variables
nome = 'Sensore-Biologico'
temperatura = random.randint(1, 40)
umidita = random.randint(1, 100)
carica_batterica = random.randint(1, 100)
date_format = "%d/%m/%Y %H:%M:%S"

log = datetime.datetime.now().strftime(date_format)

db = sqlite3.connect('Bio_Sensore.sqlite')


def start():

    with db:
        cur = db.cursor()
        try:
            cur.execute('INSERT INTO Dati_Sensore (Nome,Umidita,Carica_Batterica,Temperatura,Log) \
                VALUES (?, ?, ?, ?, ?)', (nome, str(umidita) + '%', str(carica_batterica) + '%', str(temperatura) + u"\N{DEGREE SIGN}", str(log)))
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

        finally:
            cur.close()


def analyse_data():

    with db:
        cur = db.cursor()
        try:
            for row in cur.execute('SELECT * FROM Dati_Sensore WHERE Id_Sensore = 1'):
                print(row)
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

        finally:
            cur.close()

    labels = ['Umidità', 'Carica Batterica']
    quantity = [umidita, carica_batterica]

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

    plt.pie(quantity, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)

    plt.axis('equal')

    plt.show()


def main():
    print("##################################")
    print(" Welcome to Natan's Bio-Sensor ")
    print("[1] - Start Scanning\n[2] - Check Collected Data")
    print("##################################")

    while True:
        try:
            scelta = int(input("Please enter the desired code: "))
            if scelta == 1:
                start()
                print("Scan completed and inserted into DB!")
                break
            elif scelta == 2:
                analyse_data()
                break
            else:
                print("Invalid code entered, please try again... ")
        except ValueError:
            continue

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
