import sqlite3
import random
import datetime


# Variables
nome = 'Sensore-Biologico'
temperatura = random.randint(1, 40)
umidita = random.randint(1, 100)
carica_batterica = random.randint(1, 100)
date_format = "%d/%m/%Y %H:%M:%S"
code = []

log = datetime.datetime.now().strftime(date_format)

db = sqlite3.connect('file:/Users/natan/projectwork/R&D-Analisi-Terreno/BioSensore.db?mode=rw', uri=True)


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
            for row in cur.execute('SELECT * FROM Dati_Sensore'):
                print(row)
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

        finally:
            cur.close()


def main():

    while True:
        try:
            print("##################################")
            print(" Welcome to Natan's Bio-Sensor ")
            print("[1] - Start Scanning\n[2] - Check Collected Data")
            print("##################################")
            scelta = int(input("Please enter the desired code: "))
            if scelta == 1:
                start()
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
