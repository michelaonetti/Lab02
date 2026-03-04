from dictionary import Dictionary
class Translator:

    def __init__(self):
      self.dictionary_obj = Dictionary()

    def printMenu(self):
        comandi = ["Aggiungi nuova parola", "Cerca una traduzione", "Cerca con wildcard","Stampa tutto il dizionario", "Exit"]
        i = 1
        for comando in comandi:
            print(f"{i}. {comando}")
            i=i+1


    def loadDictionary(self, dict:str):
        # dizionario_traslations[nickname] = punteggio
        # devo aprire il file e leggerlo salvarmi le informazioni nel dizionario


        file = open(dict, "r", encoding="utf-8")  # solo lettura
        righe = file.readlines()
        file.close()

        i = 0

        while i < len(righe):

            # per ogni riga , tolgo tutti gli spazi all'inixio e ealla fine della frase (strip())
            # se la riga è vuota salto
            if righe[i].strip() == "":
                i = i + 1
                continue

            # altrimenti se la riga esiste, leggo i dati della domanda
            testo_riga = righe[i].strip()  # pulisce agli estremi
            riga_pulita = testo_riga.split()  # divide la riga in due parole, una PAROLAALEINA e TRADUZIONE
            alieno = riga_pulita[0]
            traduzione = riga_pulita[1]

            self.dictionary_obj.addWord(alieno, traduzione)
            #se non c'è mi crea la lista traduzioni nuova, altrimenti aggiunge la traduzione


            i = i + 1  # vado avanti con la roga da leggere e aggiungo tutte le traduzioni in questo modo



    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        #voglio aggiungere una coppia, leggo l'input e lo aggiungo al dizionario

        entry = entry.strip()
        testo_entry = entry.split()
        if len(testo_entry)==2:
            alieno = testo_entry[0]
            traduzione = testo_entry[1]

            self.dictionary_obj.addWord(alieno, traduzione)
        else:
            alieno = testo_entry[0]

            i= 1
            traduzioni=[]
            while i < len(testo_entry):
                traduzioni.append(testo_entry[i].strip())
                i=i+1
            self.dictionary_obj.addWordList(alieno, traduzioni)





    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        #chiedo la tarduzione di quella parola aliena,
        query= query.strip()
        #la ricerco nella lista con oggetti di tipo dizionario
        return self.dictionary_obj.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        query = query.strip().lower()

        risultati = self.dictionary_obj.translateWordWildCard(query)

        if risultati:
            for r in risultati:
                print("Traduzione:", r)
        else:
            print("Nessuna parola trovata")

    def stampaTutto(self):

        for key in self.dictionary_obj.dizionario:
            print(f"{key} {self.dictionary_obj.dizionario.get(key)}")