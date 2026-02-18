# Analýza prodejů v Pythonu

Tento skript načítá data ze souboru `prodeje.txt`, čistí je a počítá celkové tržby pro jednotlivé kategorie zboží.

## Co skript umí:
* Načítá data ze středníkem odděleného textového souboru.
* Ignoruje prázdné řádky v datech.
* Pomocí `try-except` přeskočí záznamy, kde chybí cena nebo množství (např. hodnoty NULL).
* Vypočítá obrat (cena * množství) a sečte ho podle kategorií do slovníku.
* Vypočítá celkové prodeje a průměrné ceny prodejů v jednotlivých kategoriích.
* Vypíše výsledky přehledně pod sebe.

Potom mě napadlo, že by bylo lepší tyto výsledky exportovat do csv souboru. Skript jsem ještě upravila a vložila jako nový souboru "analyza_excel.py"
