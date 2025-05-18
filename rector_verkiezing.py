from verkiezing import Kandidaat, Stem, Kiezer

# RectorKandidaat klasse
class RectorKandidaat(Kandidaat):
    def __init__(self, naam):
        super().__init__(naam)

# RectorKiezer klasse
class RectorKiezer(Kiezer):
    def __init__(self, naam):
        super().__init__(naam)

    def stem(self, kandidaat):
        if isinstance(kandidaat, RectorKandidaat):
            kandidaat.geef_stem("stem")
            print("{} heeft gestemd op {}".format(self.naam, kandidaat.naam))
        else:
            print("{} kan niet stemmen op {}".format(self.naam, kandidaat.naam))

# RectorVerkiezing klasse
class RectorVerkiezing:
    def __init__(self):
        self.kandidaten = []

    def voeg_kandidaat_toe(self, naam):
        self.kandidaten.append(RectorKandidaat(naam))

    def toon_resultaten(self):
        print("\nResultaten van de rectorverkiezing:")
        for kandidaat in self.kandidaten:
            print("- {} met {} stemmen".format(kandidaat.naam, len(kandidaat.stemmen)))

# Voorbeeldgebruik
rector_verkiezing = RectorVerkiezing()

# Kandidaten toevoegen
rector_verkiezing.voeg_kandidaat_toe("Prof. Van Dam")
rector_verkiezing.voeg_kandidaat_toe("Prof. De Vries")

# Kiezers aanmaken
kiezer1 = RectorKiezer("Alice")
kiezer2 = RectorKiezer("Bob")

# Stemmen
kiezer1.stem(rector_verkiezing.kandidaten[0])  # Alice stemt op Prof. Van Dam
kiezer2.stem(rector_verkiezing.kandidaten[1])  # Bob stemt op Prof. De Vries

# Resultaten tonen
rector_verkiezing.toon_resultaten()
