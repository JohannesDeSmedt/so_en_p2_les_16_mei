class Stembus:
    def __init__(self):
        self._stemmen = []

    def voeg_toe(self, stem):
        self._stemmen.append(stem)

    def getal_stemmen(self):
        return len(self._stemmen)

    def toon_stemmen(self):
        for stem in self._stemmen:
            print(stem)

    def get_stemmen(self):
        return self._stemmen



