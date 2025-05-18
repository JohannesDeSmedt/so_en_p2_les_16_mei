from verkiezing import Kandidaat, Stem, Kiezer
import random
class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

    def __str__(self):
        return f"{self.naam} (Rector: {self.faculteit})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self.faculteit = faculteit

    def __str__(self):
        return f"Stem op {self.kandidaat} (Rector: {self.faculteit})"
    
class RectorKiezer(Kiezer):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

    def stem(self, kandidaat):
        stem = RectorStem(kandidaat, self.faculteit)
        kandidaat.geef_stem(stem)
        print(f"{self.naam} heeft gestemd op {kandidaat} ({self.faculteit})")    
   
kandidatenlijst = [
    RectorKandidaat("Siemon","Theologie en Religiewetenschappen"),
    RectorKandidaat("Jonas","Sociale Wetenschappen"),
    RectorKandidaat("Tom","Letteren"),
    RectorKandidaat("Femke","Toegepaste Economische Wetenschappen"),
    RectorKandidaat("Geert","Economie en Bedrijfswetenschappen"),
    RectorKandidaat("Wilfried","Economie en Bedrijfswetenschappen"),
]
lijst_kiezers = [
    RectorKiezer("Jos","Sociale Wetenschappen"),
    RectorKiezer("Johan","Letteren"),
    RectorKiezer("Tommeke","Economie en Bedrijfswetenschappen")
]

for kiezer in lijst_kiezers:
    #ik ga het lot laten beslissen op wie de mensen gaan stemmen:
    #kandidaatnummer die stem krijgt:
    kandidaatnummer = random.randint(0,len(kandidatenlijst)-1)
    kiezer.stem(kandidatenlijst[kandidaatnummer])
    
     
    