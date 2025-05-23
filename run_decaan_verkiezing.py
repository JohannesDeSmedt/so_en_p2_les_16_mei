import random
from decaan_verkiezing import DecaanKandidaat, DecaanKiezer

print("\nStart van decaanverkiezing\n" + "-"*30)

# Nieuwe lijst van kandidaten
lijst_van_kandidaten = [
    DecaanKandidaat("Laura", "Economie"),
    DecaanKandidaat("Sofie", "Geneeskunde"),
    DecaanKandidaat("Tom", "Rechten"),
    
]

# Nieuwe lijst van kiezers
lijst_kiezers = [
    DecaanKiezer("Jan", "Economie"),
    DecaanKiezer("Lisa", "Geneeskunde"),
    DecaanKiezer("Mark", "Psychologie"),
    DecaanKiezer("Nina", "Rechten"),
    DecaanKiezer("Joris", "Rechten"),
    DecaanKiezer("Emma", "Geneeskunde"),  
    DecaanKiezer("Eva", "Economie"),
    DecaanKiezer("Bart", "Economie"),
    DecaanKiezer("Jan", "Wiskunde"),
    DecaanKiezer("Julie", "Fysica"), 
    DecaanKiezer("Pedro", "Economie")
]

# Simulatie: elke kiezer stemt op een kandidaat van dezelfde opleiding indien mogelijk,
# anders stemt die random op een kandidaat
for kiezer in lijst_kiezers:
    kandidaten_voor_kiezer = [k for k in lijst_van_kandidaten if k.opleiding == kiezer.opleiding]
    if kandidaten_voor_kiezer:
        kiezer.stem(kandidaten_voor_kiezer[0])
    else:
        # Willekeurige kandidaat kiezen
        random_kandidaat = random.choice(lijst_van_kandidaten)
        print(f"{kiezer.naam} kan niet stemmen op opleiding {kiezer.opleiding}, want er is geen kandidaat voor die opleiding")
        kiezer.forceer_stem(random_kandidaat)

print("\nUitslag van de decaanverkiezing:")
for kandidaat in sorted(lijst_van_kandidaten, key=lambda k: k.aantal_stemmen, reverse=True):
    print(f"{kandidaat}: {kandidaat.aantal_stemmen} stemmen")


