
class Dictionary:
    def __init__(self):
        self.dizionario={}


    def addWord(self, word:str, traduzione:str):

            if word not in self.dizionario:
                traduzioni=[]
                traduzioni.append(traduzione)
                self.dizionario[word] = traduzioni
            else:
                traduzioni = self.dizionario[word]
                traduzioni.append(traduzione)
                self.dizionario[word] = traduzioni


    def addWordList(self, word:str, traduzioni:list):
        # devo verificare anche qui se sia gia uno solo o + traduzioni già possibili
        if word not in self.dizionario:
            self.dizionario[word] = traduzioni
        else:
            traduzioni_esistenti = self.dizionario[word]
            traduzioni_esistenti.extend(traduzioni)
            self.dizionario[word] = traduzioni_esistenti

    def translate(self, word:str):

        traduzioni = self.dizionario.get(word)
        return traduzioni


    def translateWordWildCard(self,pattern):
        pattern = pattern.lower()
        risultati = []

        for parola in self.dizionario:

            if len(parola) != len(pattern):
                continue

            match = True

            for i in range(len(pattern)):
                if pattern[i] != "?" and pattern[i] != parola[i]:
                    match = False
                    break

            if match:
                risultati.append(self.dizionario[parola])

        return risultati



