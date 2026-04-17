import csv
from pathlib import Path

class DataBase:
    def __init__(self, eleresi_ut):
        # A Path objektum segít a mappák kezelésében
        self.utvonal = Path(eleresi_ut)

    def beolvas(self):
        # Üres lista az adatoknak
        eredmeny = []
        
        try:
            # utf-8-sig: törli a \ufeff karaktert az elejéről
            # delimiter=';': az oszlopok szétválasztásához
            with open(self.utvonal, mode='r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f, delimiter=';')
                
                for sor in reader:
                    eredmeny.append(sor)
            
            return eredmeny

        except FileNotFoundError:
            print("Hiba: A megadott útvonalon nem található a fájl.")
            return []
        except Exception as e:
            print(f"Hiba történt: {e}")
            return []

# --- Így használd ---

# 1. Add meg az utat (vagy abszolút, vagy relatív módon)
#fajl_helye = Path(__file__).parent.parent / "data" / "order.csv"

# 2. Példányosítod és beolvasol
#loader = DataBase(fajl_helye)
#adat_lista = loader.beolvas()

# 3. Ellenőrzés: írjuk ki a beolvasott adatokat
#for adat in adat_lista:
#    print(adat['ugyfel_alias'])


