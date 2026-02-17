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
        
print("\n-- PŘEHLED TRŽEB --")
for kategorie, celkovy_obrat in obrat_kategorie.items():
    print(f"{kategorie:10}: {celkovy_obrat} Kč")

print("\n-- CELKEM PRODÁNO KUSŮ --") 
for kategorie, prodano in prodej_celkem.items():
    print(f"{kategorie:10}: {prodano} ks")
    
print("\n-- PRŮMĚRNÁ PRODEJNÍ CENA V KATEGORIÍCH --") 
for kategorie in obrat_kategorie:
    trzby = obrat_kategorie[kategorie]
    kusy = prodej_celkem[kategorie]
    
    prumer = trzby / kusy
    print(f"{kategorie:10}: {prumer: .2f} Kč")