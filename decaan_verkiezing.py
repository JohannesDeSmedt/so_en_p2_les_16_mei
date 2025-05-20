from verkiezing import Kandidaat, Stem, Kiezer
import random
#from faker import Faker

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam_kandidaat, opleiding):
        super().__init__(naam_kandidaat)
        self.__opleiding = opleiding
    
    @property
    def get_opleiding(self):
        return self.__opleiding

    def __str__(self):
        return super().__str__() + self.get_opleiding
    
class DecaanStem(Stem):
    def __init__(self, kandidaat: DecaanKandidaat, opleiding):
        super().__init__(kandidaat)
        self.__opleiding = opleiding

    @property
    def get_opleiding(self):
        return self.__opleiding

    def __str__(self):
        return super().__str__() + self.get_opleiding
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.__opleiding = opleiding
    
    @property
    def get_opleiding(self):
        return self.__opleiding

    def stem(self, kandidaat: DecaanKandidaat):
        if kandidaat.get_opleiding == self.get_opleiding:
            stem = DecaanStem(kandidaat, self.get_opleiding) #overschrijft niet, maakt telkens nieuw object aan
            kandidaat.geef_stem(stem)
            print(f"{self.get_naam_kiezer} ({self.get_opleiding}) heeft gestemd op {kandidaat.get_naam_kandidaat} ({self.get_opleiding})")
        else:
            print(f"{self.get_naam_kiezer} ({self.get_opleiding}) kan niet stemmen op {kandidaat.get_naam_kandidaat} ({kandidaat.get_opleiding})")
    
    def __str__(self):
        return super().__str__()
        
#kandidatenlijst
kandidatenlijst = [
    DecaanKandidaat("Laura", "Biotechnologie"),
    DecaanKandidaat("Michaël", "Artificiële Intelligentie"),
    DecaanKandidaat("Sanne", "Bedrijfskunde"),
    DecaanKandidaat("Lars", "Milieuwetenschappen"),
    DecaanKandidaat("Eline", "Neurowetenschappen"),
    DecaanKandidaat("Daan", "Handelsingenieur")
]

#kiezerslijst
random.seed(42)
'''vakken = ['Biotechnologie', 'Artificiële Intelligentie', 'Bedrijfskunde', 'Milieuwetenschappen', 'Neurowetenschappen', 'Handelsingenieur']
fake = Faker('nl_NL')
kiezerslijst = []
for i in range(50):
    kiezerslijst.append(DecaanKiezer(fake.first_name(), random.choice(vakken)))'''

kiezerslijst = [
    DecaanKiezer("Anna", "Bedrijfskunde"),
    DecaanKiezer("Victor", "Handelsingenieur"),
    DecaanKiezer("Nora", "Biotechnologie"),
    DecaanKiezer("Jan", "Neurowetenschappen")
]

#Stemprocedure
stemmen = []
for kiezer in kiezerslijst:
    random_kandidaat = random.randint(0, len(kandidatenlijst) - 1)
    kiezer.stem(kandidatenlijst[random_kandidaat]) #hier zijn beide kiezer en kandidatenlijst[random_kandidaat] objecten

for kandidaat in kandidatenlijst:
    print(f'{kandidaat} heeft zoveel stemmen: {len(kandidaat.get_stemmen)}')
