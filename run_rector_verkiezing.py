from rector_verkiezing import RectorKiezer, RectorKandidaat
from stembus import Stembus

print("Start van de rectorverkiezing")
print("=" * 40) 

kandidaten = [
    RectorKandidaat("Alice", "Letteren"),
    RectorKandidaat("Bob", "Geneeskunde"),
    RectorKandidaat("Charlie", "Geneeskunde"),
    RectorKandidaat("Diana", "Economie"),
    RectorKandidaat("Erik", "Economie")
]

kiezers = [
    RectorKiezer("Jan"),
    RectorKiezer("Marie"),
    RectorKiezer("Tom"),
    RectorKiezer("Sofie"),
    RectorKiezer("Lukas")
]

stembus = Stembus()

for kiezer in kiezers:
    kiezer.stem(kandidaten, stembus)

print("\nOverzicht van alle stemmen die in de stembus zitten:")
stembus.toon_stemmen()

print("\nResultaat van de rectorverkiezing:")
stemmen_per_kandidaat = {}

for stem in stembus.get_stemmen():
    kandidaat = stem.kandidaat
    if kandidaat not in stemmen_per_kandidaat:
        stemmen_per_kandidaat[kandidaat] = 0
    stemmen_per_kandidaat[kandidaat] += 1

for kandidaat, aantal_stemmen in sorted(stemmen_per_kandidaat.items(), key=lambda x: x[1], reverse=True):
    print(f"{kandidaat}: {aantal_stemmen} stemmen")





