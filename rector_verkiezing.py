from verkiezing import Kandidaat, Stem, Kiezer
import random
from faker import Faker

class RectorKandidaat(Kandidaat):
    def __init__(self, naam_kandidaat, faculteit):
        super().__init__(naam_kandidaat)
        self.__faculteit = faculteit

    @property
    def get_faculteit(self):
        return self.__faculteit

    def __str__(self):
        return super().__str__() + self.get_faculteit
    
class RectorStem(Stem):
    def __init__(self, kandidaat: RectorKandidaat, faculteit):
        super().__init__(kandidaat)
        self.__faculteit = faculteit

    @property
    def get_faculteit(self):
        return self.__faculteit

    def __str__(self):
        return super().__str__() + self.get_faculteit
    
class RectorKiezer(Kiezer):
    def __init__(self, naam_kiezer, faculteit):
        super().__init__(naam_kiezer)
        self.__faculteit = faculteit

    @property
    def get_faculteit(self):
        return self.__faculteit
    
    def stem(self, kandidaat: RectorKandidaat):
        if kandidaat.get_faculteit == self.get_faculteit:
            stem = RectorStem(kandidaat, self.get_faculteit)
            kandidaat.geef_stem(stem)
            print(f"{self.get_naam_kiezer} ({self.get_faculteit}) heeft gestemd op {kandidaat.get_naam_kandidaat} ({self.get_faculteit})")
        else:
            print(f"{self.get_naam_kiezer} ({self.get_faculteit}) kan niet stemmen op {kandidaat.get_naam_kandidaat} ({kandidaat.get_faculteit})")
    
    def __str__(self):
        return super().__str__()
    

#kandidatenlijst
kandidatenlijst = [
    RectorKandidaat("Laura", "FEB"),
    RectorKandidaat("Michaël", "Faculteit architectuur"),
    RectorKandidaat("Sanne", "Faculteit letteren"),
    RectorKandidaat("Lars", "Faculteit wetenschappen"),
    RectorKandidaat("Eline", "Faculteit geneeskunde"),
    RectorKandidaat("Daan", "FEB")
]

#kiezerslijst
random.seed(42)
faculteiten = ['FEB', 'Faculteit geneeskunde', 'Faculteit wetenschappen', 'Faculteit architectuur', 'Faculteit letteren']
fake = Faker('nl_NL')
kiezerslijst = []
for i in range(50):
    kiezerslijst.append(DecaanKiezer(fake.first_name(), random.choice(faculteiten)))

'''kiezerslijst = [
    RectorKiezer("Anna", "FEB"),
    RectorKiezer("Victor", "Faculteit geneeskunde"),
    RectorKiezer("Nora", "Faculteit wetenschappen"),
    RectorKiezer("Jan", "FEB")
]'''

#Stemprocedure
stemmen = []
for kiezer in kiezerslijst:
    random_kandidaat = random.randint(0, len(kandidatenlijst) - 1)
    kiezer.stem(kandidatenlijst[random_kandidaat]) #hier zijn beide kiezer en kandidatenlijst[random_kandidaat] objecten

for kandidaat in kandidatenlijst:
    print(f'{kandidaat} heeft zoveel stemmen: {len(kandidaat.get_stemmen)}')