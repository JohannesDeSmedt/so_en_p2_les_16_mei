from decaan_verkiezing import DecaanKandidaat, DecaanKiezer, DecaanVerkiezing

def main():
    verkiezing = DecaanVerkiezing()

    # Kandidaten toevoegen
    verkiezing.voeg_kandidaat_toe(DecaanKandidaat("Anna", "Informatica"))
    verkiezing.voeg_kandidaat_toe(DecaanKandidaat("Bas", "Economie"))
    verkiezing.voeg_kandidaat_toe(DecaanKandidaat("Claudia", "Informatica"))

    # Kiezers toevoegen
    verkiezing.voeg_kiezer_toe(DecaanKiezer("Eva", "Informatica"))
    verkiezing.voeg_kiezer_toe(DecaanKiezer("Jan", "Economie"))
    verkiezing.voeg_kiezer_toe(DecaanKiezer("Lars", "Informatica"))

    # Stemmen laten plaatsvinden
    verkiezing.laat_stemmen()

    # Optioneel: toon aantal stemmen per kandidaat
    for kandidaat in verkiezing._kandidaten:
        print(f"{kandidaat} heeft {len(kandidaat.stemmen)} stemmen")

if __name__ == "__main__":
    main()