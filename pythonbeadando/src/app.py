

from csv_reader import DataBase
from pathlib import Path

class App():
        MENU = """
                1) Kilistázások
                2) Rekordok kezelése
                3) Keresések
                q) quit
                """
        Lista_MENU = """
                1) Rendelések
                2) Feltétek
                3) Vélemények
                v) vissza
        """
        def __init__(self, filepath):

                if (filepath == "data/order.csv"):
                        order = DataBase(separator=';')
                        self.__order= order.rendeles_beolvas(filepath)
                elif (filepath == "data/dressing.csv"):
                        dre = DataBase(separator=';')
                        self.__dressing= dre.dressing_beolvas(filepath)
                else:
                        rev = DataBase(separator=';')
                        self.__review= rev.review_beolvas(filepath)
                
        def list_order(order):

                print(f"\n{'ID':<2} | {'Ügyfél Alias':<20} | {'Méret':<15} | {'Tej típus':<15} | {'Szirupok Száma':<15} | {'Hab Jelző':<15} | {'Összetevők Száma':<15} | {'Ár':<15}\n")
                for o in order.__order:
                        print(o)

        def list_dressing(dressing):

                print(f"\n{'Tétel ID':<2} | {'Rendelés ID':<12} | {'Összetvő':<16} | {'Kategória':<15} | {'Extra-e':<5}\n")
                for d in dressing.__dressing:
                        print(d)

        def list_review(review):
                
                print(f"\n{'Értékelés ID':<15} | {'Rendelési ID':<15} | {'Várakozási idő (perc)':<22} | {'Elegedettség':<15} | {'Újrarendelné-e':<15} | {'Barista Megjegyzése':<30}\n")
                for r in review.__review:
                        print(r)               

        def run(self):
                while True:
                        print("="*20 + "  +++  " + "="*20)
                        print(self.MENU)
                        valasz = input("==> ")
                        match valasz:
                                case "1":
                                        print(self.Lista_MENU)
                                        listazas_valasz = input("==> ")
                                        match listazas_valasz:
                                                case "1":
                                                        self.list_order(App("data/order.csv"))
                                                case "2":
                                                        self.list_dressing(App("data/dressing.csv"))
                                                case "3":
                                                        self.list_review(App("data/review.csv"))
                                                case "v":
                                                        continue
                                case "2":
                                        #rekord kezelés
                                        return
                                case "3":
                                        #Keresés
                                        return
                                case "q":
                                        return
        
        

        
                        
                     
    