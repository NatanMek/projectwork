import sqlite3
import datetime

conn = sqlite3.connect('tornelli.db')

date_format = "%d/%m/%Y %H:%M:%S"
data = datetime.datetime.now().strftime(date_format)


def setUser(_nome, _cognome, _cf, _indirizzo):
    c = conn.cursor()
    try:
        c.execute("INSERT INTO [Utente](Nome,Cognome,CF,Indirizzo) VALUES (?,?,?,?)",
                  (_nome, _cognome, _cf, _indirizzo))

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite tab", error)
    finally:
        c.close()


def setUserRole(r):
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO [RuoloUtente](Ruolo,Utente) VALUES ((SELECT IDruolo FROM [Ruolo] WHERE Nome = ?),(SELECT max (IDutenteBadge) FROM [Utente]))",
            [r])

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite tab", error)
    finally:
        c.close()


def newBadge():
    nome = input('Nome: ')
    cognome = input('Cognome: ')

    while True:
        cf = input('Codice Fiscale: ')
        with conn:
            c = conn.cursor()
            try:
                c.execute("SELECT CF FROM [Utente]")
                check = c.fetchall()

            except sqlite3.Error as error:
                print("Failed to insert data into sqlite table", error)

            finally:
                c.close()
        cont = 0
        for i in range(len(check)):
            if cf == check[i][0]:
                cont = cont + 1
        if cont == 1:
            print("Codice fiscale già presente!")
        else:
            break

    ind = input('Indirizzo: ')

    while True:
        ruolo = input("Ruolo: ")
        with conn:
            cursore = conn.cursor()
            try:
                cursore.execute("SELECT Nome FROM [Ruolo]")
                ctrl = cursore.fetchall()

            except sqlite3.Error as error:
                print("Failed to insert data into sqlite table", error)

            finally:
                cursore.close()
        cont = 0
        for i in range(len(ctrl)):
            if ruolo == ctrl[i][0]:
                cont = cont + 1
        if cont == 1:
            break
        else:
            print(f"Immettere un Ruolo esistente! {ctrl}")

    setUser(nome, cognome, cf, ind)
    setUserRole(ruolo)
    with conn:
        c = conn.cursor()
        try:
            c.execute("SELECT max (IDutenteBadge) FROM [Utente]")
            ck = c.fetchone()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        finally:
            c.close()

        print('Operazione andata a buon fine! Il suo numero badge è:', ck)


def access():
    while True:
        room = str(input('In quale stanza desidera accedere?'))
        with conn:
            cursore = conn.cursor()
            try:
                cursore.execute("SELECT Nome FROM [Stanza]")
                righe = cursore.fetchall()

            except sqlite3.Error as error:
                print("Failed to insert data into sqlite table", error)

            finally:
                cursore.close()
        cont = 0
        for i in range(len(righe)):
            if room == righe[i][0]:
                cont = cont + 1
        if cont == 1:
            break
        else:
            print(f"Immettere una stanza esistente! {righe}")

    while True:
        numero = int(input('Inserire numero Badge: '))
        with conn:
            c = conn.cursor()
            try:
                c.execute("SELECT IDutenteBadge FROM [Utente]")
                riga = c.fetchall()
                c.execute("SELECT Cognome FROM Utente WHERE IDutenteBadge = ?", (numero,))
                d = c.fetchone()
            except sqlite3.Error as error:
                print("Failed to insert data into sqlite table", error)
            finally:
                c.close()
        cont = 0
        for i in range(len(riga)):
            if numero == riga[i][0]:
                cont = cont + 1
        if cont >= 1:
            break
        else:
            print("Numero badge inesistente")
    with conn:
        c = conn.cursor()
        try:
            c.execute(
                "SELECT Ruolo.Nome FROM Ruolo join RuoloUtente on Ruolo.IDruolo=RuoloUtente.Ruolo WHERE RuoloUtente.Utente = ?",
                (numero,))
            r = c.fetchone()
            c.execute(
                "INSERT INTO [Accesso](Stanza,Utente,data_ora) VALUES ((SELECT IDstanza FROM Stanza WHERE Nome=?),(?),(?))",
                (room, numero, data,))
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        finally:
            c.close()

    print("Benvenuto/a:", d, 'Ruolo:', r)
    print("Accesso effettuato il:", data)


def main():
    while True:
        print(
            ' \n ( 1 ) Entra nel Tornello\n ( 2 ) Crea Nuovo Badge\n')
        scelta = int(input("-> "))
        if scelta == 1:
            access()

        if scelta == 2:
            newBadge()


main()
