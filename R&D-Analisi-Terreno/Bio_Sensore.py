import datetime
import random
import sqlite3
import time
import plotly.graph_objects as go

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
            print(
                f"Scan completed. This is the data inserted into DB:\n Nome: {nome}\n Temperatura: {temperatura}\N{DEGREE SIGN}\n Umidità: {umidita}%\n Carica Batterica: {carica_batterica}%\n Data: {log}")
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

        finally:
            cur.close()


def fetch_data():

    with db:
        cur = db.cursor()
        try:
            cur.execute('SELECT * FROM Dati_Sensore')
            result = cur.fetchall()
            for row in result:
                print(f'\n Nome: {row[1]}\n Umidità: {row[2]}\n Carica Batterica: {row[3]}\n Temperatura: {row[4]}\n Data: {row[5]}')
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

        finally:
            cur.close()

    cities = ['Milano', 'Torino', 'Roma', 'Napoli', 'Venezia']

    fig = go.Figure(data=[
        go.Bar(name='Umidità', x=cities, y=[result[0][2], result[1][2], result[2][2], result[3][2], result[4][2]]),
        go.Bar(name='Carica Batterica', x=cities, y=[result[0][3], result[1][3], result[2][3], result[3][3], result[4][3]]),
        go.Bar(name='Temperatura', x=cities, y=[result[0][4], result[1][4], result[2][4], result[3][4], result[4][4]])
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()


def updateStart(total, progress):

    bar_length, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(bar_length * progress))
    text = "\r[{}] {:.0f}% {} Analyzing soil...".format(
        "#" * block + "-" * (bar_length - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()


runs = 30


def updateFetchData(total, progress):

    bar_length, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(bar_length * progress))
    text = "\r[{}] {:.0f}% {} Fetching Data...".format(
        "#" * block + "-" * (bar_length - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()


runs = 30


def main():
    print("##################################")
    print(" Welcome to Natan's Bio-Sensor ")
    print("[1] - Start Scanning\n[2] - Fetch Data")
    print("##################################")

    while True:
        try:
            scelta = int(input("Please enter the desired code: "))
            if scelta == 1:
                for run_num in range(runs):
                    time.sleep(.1)
                    updateStart(runs, run_num + 1)
                start()
                break
            elif scelta == 2:
                for run_num in range(runs):
                    time.sleep(.1)
                    updateFetchData(runs, run_num + 1)
                print("Fetching Completed!")
                fetch_data()
                break
            else:
                print("Invalid code entered, please try again... ")
        except ValueError:
            continue

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
