from verkiezing import Kandidaat, Stem, Kiezer

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self._opleiding = opleiding

    def get_opleiding(self):
        return self._opleiding
    
    def __str__(self):
        return f"{self.get_naam()} ({self._opleiding})"
    
class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self._opleiding = opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self._opleiding})"
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self._opleiding = opleiding

    def get_opleiding(self):
        return self._opleiding

    def stem(self, kandidaat):
        if kandidaat.get_opleiding() == self._opleiding:
            stem = DecaanStem(kandidaat, self._opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.get_naam()} heeft gestemd op {kandidaat} ({self._opleiding})")
        else:
            print(f"{self.get_naam()} kan niet stemmen op {kandidaat} ({kandidaat.get_opleiding()})")

class Verkiezing:
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
        return True
    
class DecaanVerkiezing(Verkiezing):
    def mag_stemmen(self, kiezer, kandidaat):
        return kiezer.get_opleiding() == kandidaat.get_opleiding()