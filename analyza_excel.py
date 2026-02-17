obrat_kategorie = dict()
prodej_celkem = dict()

with open ("prodeje.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if len(line) < 1: continue
        casti = line.split(";")
        try:
            produkt = casti[0]
            cena = int(casti[1])
            kategorie = casti[2]
            prodane_mn = int(casti[3])
            
            obrat = prodane_mn * cena
            
            obrat_kategorie[kategorie] = obrat_kategorie.get(kategorie, 0) + obrat
            prodej_celkem[kategorie] = prodej_celkem.get(kategorie, 0) + prodane_mn
            
        except:
            print(f'Přeskakuji chybný záznam {line}')
            continue
        
vystup = "report_trzeb.csv"

with open("report_trzeb.csv", mode="w", encoding="utf-8") as out_file:
    out_file.write("Kategorie;Celkovy obrat;Pocet kusu;Průměrná cena\n")
    for kategorie in obrat_kategorie:
        trzby = obrat_kategorie[kategorie]
        kusy = prodej_celkem[kategorie]
        prumer = trzby / kusy
        
        radek = f"{kategorie};{trzby};{kusy};{prumer:.2f}\n"
        
        out_file.write(radek)

print(f'Hotovo! Report byl uložen do souboru {vystup}')