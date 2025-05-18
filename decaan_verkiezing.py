from verkiezing import Kandidaat, Stem, Kiezer

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def __str__(self):
        return "Kandidaat: {} (Opleiding: {})".format(self.naam, self.opleiding)

class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def stem(self, kandidaat):
        if isinstance(kandidaat, DecaanKandidaat) and kandidaat.opleiding == self.opleiding:
            kandidaat.geef_stem("stem")
            print("{} heeft gestemd op {} (Opleiding: {})".format(self.naam, kandidaat.naam, self.opleiding))
        else:
            print("{} mag niet stemmen op {} (andere opleiding)".format(self.naam, kandidaat.naam))

# Test
decaan1 = DecaanKandidaat("Jan", "Informatica")
decaan2 = DecaanKandidaat("Piet", "Wiskunde")
kiezer1 = DecaanKiezer("Alice", "Informatica")
kiezer2 = DecaanKiezer("Bob", "Wiskunde")

kiezer1.stem(decaan1)  # Geldig
kiezer2.stem(decaan1)  # Ongeldig
