from verkiezing import Kandidaat, Stem, Kiezer

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self._faculteit = faculteit

    def get_faculteit(self):
        return self._faculteit

    def __str__(self):
        return f"{self.get_naam()} (Rector: {self._faculteit})"

class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self._faculteit = faculteit

    def get_faculteit(self):
        return self._faculteit

    def __str__(self):
        return f"Stem op {self.get_kandidaat()} (Rector: {self._faculteit})"

class RectorKiezer(Kiezer):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self._faculteit = faculteit

    def get_faculteit(self):
        return self._faculteit

    def stem(self, kandidaat):
        if kandidaat.get_faculteit() == self._faculteit:
            stem = RectorStem(kandidaat, self._faculteit)
            kandidaat.geef_stem(stem)
            print(f"{self.get_naam()} heeft gestemd op {kandidaat} ({self._faculteit})")
        else:
            print(f"{self.get_naam()} kan niet stemmen op {kandidaat} ({kandidaat.get_faculteit()})")

class RectorVerkiezing:
    def __init__(self):
        self._kandidaten = []
        self._kiezers = []

    def voeg_kandidaat_toe(self, kandidaat):
        self._kandidaten.append(kandidaat)

    def voeg_kiezer_toe(self, kiezer):
        self._kiezers.append(kiezer)

    def laat_stemmen(self):
        for kiezer in self._kiezers:
            for kandidaat in self._kandidaten:
                if self.mag_stemmen(kiezer, kandidaat):
                    kiezer.stem(kandidaat)
                    break

    def mag_stemmen(self, kiezer, kandidaat):
        return kiezer.get_faculteit() == kandidaat.get_faculteit()