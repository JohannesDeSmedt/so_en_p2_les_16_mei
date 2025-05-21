class Kandidaat:
    def __init__(self, naam):
        self.naam = naam
        self.stemmen = []

    def geef_stem(self, stem):
        self.stemmen.append(stem)

    def aantal_stemmen(self):
        return len(self.stemmen)

    def __str__(self):
        return f"{self.naam}"
    
class Stem:
    def __init__(self, kandidaat):
        self.kandidaat = kandidaat

    def __str__(self):
        return f"Stem op {self.kandidaat}"
    
class Kiezer:
    def __init__(self, naam):
        self.naam = naam


    def stem(self, kandidaat):
        stem = Stem(kandidaat)
        kandidaat.geef_stem(stem)
        print(f"{self.naam} heeft gestemd op {kandidaat}")

if __name__ == "__main__":
    k1 = Kandidaat("Laura")
    k2 = Kandidaat("Raph")
    kiezer1 = Kiezer("Thibault")
    kiezer2 = Kiezer("Alexander")

    kiezer1.stem(k1)
    kiezer2.stem(k2)
    kiezer1.stem(k1)

    print(f"{k1} heeft {k1.aantal_stemmen()} stemmen.")
    print(f"{k2} heeft {k2.aantal_stemmen()} stemmen.")
