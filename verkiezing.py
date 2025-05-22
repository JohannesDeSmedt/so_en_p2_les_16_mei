class Kandidaat:
    def __init__(self, naam):
        self._naam = naam
        self.stemmen = []

    def get_naam(self):
        return self._naam

    def geef_stem(self, stem):
        self.stemmen.append(stem)

    def __str__(self):
        return f"{self._naam}"
    
class Stem:
    def __init__(self, kandidaat):
        self.kandidaat = kandidaat

    def __str__(self):
        return f"Stem op {self.kandidaat}"
    
class Kiezer:
    def __init__(self, naam):
        self._naam = naam

    def get_naam(self):
        return self._naam

    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self._naam} heeft gestemd op {kandidaat}")
