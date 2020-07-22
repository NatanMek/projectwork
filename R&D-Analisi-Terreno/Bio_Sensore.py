import sys
import time
import sqlite3
import random
import datetime


# Variables
nome = 'Sensore-Biologico'
temperatura = random.randint(1, 100)
umidita = random.randint(1, 40)
carica_batterica = random.randint(1, 100)
date_format = "%d/%m/%Y %H:%M:%S"

log = datetime.datetime.now().strftime(date_format)

db = sqlite3.connect('BioSensore.db')
cur = db.cursor()

with db:
    try:
        cur.execute("INSERT INTO Dati_Sensore (Nome,Umidita,Carica_Batterica,Temperatura,Log) \
                VALUES (?, ?, ?, ?, ?)", (nome, str(umidita) + '%', str(carica_batterica) + '%', str(temperatura) + u"\N{DEGREE SIGN}", str(log)))
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        cur.close()

with db:
    try:
        cur.execute("SELECT * FROM Dati_Sensore")
        result = cur.fetchall()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        cur.close()

for i in range(len(result)):
    print(result)
