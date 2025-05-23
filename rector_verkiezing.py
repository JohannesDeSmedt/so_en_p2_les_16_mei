from verkiezing import Kandidaat, Stem, Kiezer

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self._faculteit = faculteit

    def __str__(self):
        return f"{self.naam} ({self._faculteit})"

class RectorStem(Stem):
    def __init__(self, kiezer, kandidaat):
        super().__init__(kiezer, kandidaat)

class RectorKiezer(Kiezer):
    MAX_STEMMEN = 3

    def __init__(self, naam):
        super().__init__(naam)

    def stem(self, kandidaten, stembus):
        import random
        gekozen_kandidaten = random.sample(kandidaten, self.MAX_STEMMEN)
        for kandidaat in gekozen_kandidaten:
            stem = RectorStem(self, kandidaat)
            stembus.voeg_toe(stem)
            print(f"{self.naam} stemde op {kandidaat}")


    