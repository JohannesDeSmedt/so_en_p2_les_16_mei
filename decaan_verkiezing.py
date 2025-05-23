from verkiezing import Kandidaat, Stem, Kiezer

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self._opleiding = opleiding

    @property
    def opleiding(self):
        return self._opleiding

    def __str__(self):
        return f"{self.naam} ({self._opleiding})"


class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self._opleiding = opleiding

    @property
    def opleiding(self):
        return self._opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self._opleiding})"


class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self._opleiding = opleiding
        self._heeft_gestemd = False

    @property
    def opleiding(self):
        return self._opleiding

    def stem(self, kandidaat):
        if self._heeft_gestemd:
            print(f"{self.naam} heeft al gestemd en kan niet opnieuw stemmen.")
            return
        if kandidaat.opleiding == self._opleiding:
            stem = DecaanStem(kandidaat, self._opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} ({self._opleiding}) heeft gestemd op {kandidaat}")
            self._heeft_gestemd = True
        else:
            print(f"{self.naam} ({self._opleiding}) kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")

    def forceer_stem(self, kandidaat):
        # Stem zonder opleiding-check, voor random stemmers
        if self._heeft_gestemd:
            print(f"{self.naam} heeft al gestemd en kan niet opnieuw stemmen.")
            return
        stem = DecaanStem(kandidaat, self._opleiding)
        kandidaat.geef_stem(stem)
        print(f"{self.naam} ({self._opleiding}) heeft random gestemd op {kandidaat}")
        self._heeft_gestemd = True


