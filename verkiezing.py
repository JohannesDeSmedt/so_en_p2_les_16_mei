class Kandidaat:
    def __init__(self, naam):
        self._naam = naam
        self._stemmen = []

    def get_naam(self):
        return self._naam

    def geef_stem(self, stem):
        self._stemmen.append(stem)

    def get_stemmen(self):
        return self._stemmen

    def __str__(self):
        return f"{self._naam}"
    
class Stem:
    def __init__(self, kandidaat):
        self._kandidaat = kandidaat

    def get_kandidaat(self):
        return self._kandidaat

    def __str__(self):
        return f"Stem op {self._kandidaat}"
    
class Kiezer:
    def __init__(self, naam):
        self._naam = naam

    def get_naam(self):
        return self._naam

    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self.get_naam()} heeft gestemd op {kandidaat}")