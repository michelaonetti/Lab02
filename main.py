import translator as tr
#Realizzare in linguaggio Python una semplice applicazione che funga da traduttore di parole aliene.
# Deve essere possibile sia l’aggiunta di nuove parole che la ricerca di quelle esistenti.
# L’applicazione dovrà essere dotata di un menù stampato su terminale, tramite il quale l’utente può
# selezionare la funzionalità richiesta digitando il numero corrispondente.
# Le funzionalità del programma richieste sono:
# - Leggere un dizionario iniziale dal file “dictionary.txt”
# - Inserire una nuova parola e la relativa traduzione secondo il seguente pattern:
# <parola aliena> <traduzione> (separate da uno spazio)
# Alla pressione del tasto invio, la parola e la sua traduzione verranno aggiunte al dizionario.
# - Cercare la traduzione di una parola esistente inserendo <parola aliena> e facendo pressione sul tasto
# invio. La traduzione verrà visualizzata sul terminale.

t = tr.Translator() #ho creato t classe Traslator


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("cosa vuoi fare? ")

    # Add input control here!
    if int(txtIn)<1 or int(txtIn)>5:
        print("Inserimento errato, riprova!")


    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        parola_tradition = input("inserisci: ")

        parola_tradition = parola_tradition.lower().strip()

        t.handleAdd(parola_tradition)
        print("aggiunto!")


    if int(txtIn) == 2:
        print("Ok, quale parola devo cercarne la traduzione?" )
        parolaDaCercare = input("inserisci: ")
        #devo leggere il file e cercare in tutte le righe se e presnete quella parola

        print(f"traduzione: {t.handleTranslate(parolaDaCercare.lower().strip())}")

    if int(txtIn) == 3:
        print("Ok, quale wildcard devo cercare?")
        parola = input("inserisci: ")


    if int(txtIn) == 4:
        print("stampo tutto il dizionario:")
        t.stampaTutto()

    if int(txtIn) == 5:
        break

