from csv import DictReader
from pathlib import Path
from orders import Order
from dressing import Dressing
from review import Review
from abc import ABC
class DataReader(ABC):
    def read(self, filename: str) -> list[Order]:
        pass

class DataBase(DataReader):
    def __init__(self, separator=";"):
        # A Path objektum segít a mappák kezelésében
        #self.utvonal = Path(eleresi_ut)
        super().__init__()

    def rendeles_beolvas(self, filename):
        # Üres lista az adatoknak
        print("Olvasas indul")
        
        try:
            # utf-8-sig: törli a \ufeff karaktert az elejéről
            # delimiter=';': az oszlopok szétválasztásához
            eredmeny = []
            with open(filename, encoding='utf-8-sig') as f:
                reader = DictReader(f, delimiter=';')
                
                for sor in reader:
                    uj_rendeles = Order(
                            sor["rendeles_id"], 
                            sor["ugyfel_alias"], 
                            sor["ital_meret"], 
                            sor["tejtipus"],  
                            sor["szirupok_szama"], 
                            sor["hab_jelzo"], 
                            sor["ossz_osszetevo"],
                            sor["ar_ft"]
                        )
                    eredmeny.append(uj_rendeles)

            return eredmeny

        except FileNotFoundError:
            print("Hiba: A megadott útvonalon nem található a fájl.")
            return []
        except Exception as e:
            print(f"Hiba történt: {e}")
            return []
        
    def dressing_beolvas(self, filename):

        print("Olvasas indul")
        
        try:
            # utf-8-sig: törli a \ufeff karaktert az elejéről
            # delimiter=';': az oszlopok szétválasztásához
            eredmeny = []
            with open(filename, encoding='utf-8-sig') as f:
                reader = DictReader(f, delimiter=';')
                
                for sor in reader:
                    dre = Dressing(
                            sor["rendeles_id"], 
                            sor["tetel_id"], 
                            sor["osszetevo"], 
                            sor["kategori"],  
                            sor["extra_e"], 
                        )
                    eredmeny.append(dre)

            return eredmeny

        except FileNotFoundError:
            print("Hiba: A megadott útvonalon nem található a fájl.")
            return []
        except Exception as e:
            print(f"Hiba történt: {e}")
            return []
        
    def review_beolvas(self, filename):
        try:
            # utf-8-sig: törli a \ufeff karaktert az elejéről
            # delimiter=';': az oszlopok szétválasztásához
            eredmeny = []
            with open(filename, encoding='utf-8-sig') as f:
                reader = DictReader(f, delimiter=';')
                
                for sor in reader:
                    rev = Review(
                            sor["ertekeles_id"], 
                            sor["rendeles_id"], 
                            sor["varakozasi_ido_perc"], 
                            sor["elegedettseg_1_10"],
                            sor["ujrarendeli_e"],  
                            sor["barista_megjegyzes"], 
                        )
                    eredmeny.append(rev)

            return eredmeny

        except FileNotFoundError:
            print("Hiba: A megadott útvonalon nem található a fájl.")
            return []
        except Exception as e:
            print(f"Hiba történt: {e}")
            return []



