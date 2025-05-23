class Kandidaat:
    def __init__(self, naam):
        self._naam = naam

    @property
    def naam(self):
        return self._naam

    def __str__(self):
        return f"{self._naam}"

class Stem:
    def __init__(self, kiezer, kandidaat):
        self._kiezer = kiezer
        self._kandidaat = kandidaat

    @property
    def kiezer(self):
        return self._kiezer

    @property
    def kandidaat(self):
        return self._kandidaat

    def __str__(self):
        return f"Stem van {self.kiezer} op {self.kandidaat}"

class Kiezer:
    def __init__(self, naam):
        self._naam = naam
        self._stemmen_gegeven = 0

    @property
    def naam(self):
        return self._naam

    def __str__(self):
        return f"{self._naam}"


