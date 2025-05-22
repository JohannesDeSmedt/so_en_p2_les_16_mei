from rector_verkiezing import RectorKandidaat, RectorKiezer, RectorVerkiezing

def main():
    verkiezing = RectorVerkiezing()

    # Kandidaten toevoegen
    verkiezing.voeg_kandidaat_toe(RectorKandidaat("Emma", "Letteren"))
    verkiezing.voeg_kandidaat_toe(RectorKandidaat("Tom", "Rechten"))
    verkiezing.voeg_kandidaat_toe(RectorKandidaat("Sara", "Letteren"))

    # Kiezers toevoegen
    verkiezing.voeg_kiezer_toe(RectorKiezer("Lotte", "Letteren"))
    verkiezing.voeg_kiezer_toe(RectorKiezer("Bram", "Rechten"))
    verkiezing.voeg_kiezer_toe(RectorKiezer("Noor", "Letteren"))

    # Stemmen laten plaatsvinden
    verkiezing.laat_stemmen()

    # Stemmen tonen per kandidaat
    for kandidaat in verkiezing._kandidaten:
        print(f"{kandidaat} heeft {len(kandidaat.get_stemmen())} stemmen")

if __name__ == "__main__":
    main()