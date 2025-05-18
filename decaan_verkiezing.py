from verkiezing import Kandidaat, Stem, Kiezer
import random
class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def __str__(self):
        return f"{self.naam} ({self.opleiding})"
    
class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self.opleiding = opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self.opleiding})"
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self.opleiding:
            stem = DecaanStem(kandidaat, self.opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} heeft gestemd op {kandidaat} ({self.opleiding})")
        else:
            print(f"{self.naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")

kandidatenlijst = [
    DecaanKandidaat("Siemon","Kinesitherapie"),
    DecaanKandidaat("Jonas","Informatica"),
    DecaanKandidaat("Tom","Handelsingenieur"),
    DecaanKandidaat("Femke","Toegepaste Economische Wetenschappen"),
    DecaanKandidaat("Geert","Psychologie"),
    DecaanKandidaat("Wilfried","Marketing"),
]
lijst_kiezers = [
    DecaanKiezer("Jos","Handelsingenieur"),
    DecaanKiezer("Johan","Marketing"),
    DecaanKiezer("Tommeke","Psychologie")
]

for kiezer in lijst_kiezers:
    #ik ga het lot laten beslissen op wie de mensen gaan stemmen:
    #kandidaatnummer die stem krijgt:
    kandiddaatnummer = random.randint(0,len(kandidatenlijst)+1)
        kiezer.stem(kandidatenlijst[kandidaatnummer])
    
    
