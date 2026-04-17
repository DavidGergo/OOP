

from csv_reader import DataBase
from pathlib import Path

class App():
        MENU = """
                1) Rendelések kilistázása
                2) Feltétek kilistázása
                3) Vélemények kilistázása
                q) quit
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
                        self.__review= rev.rendeles_beolvas(filepath)
                
        def list_order(order):

                print(f"\n{'ID':<2} | {'Ügyfél Alias':<20} | {'Méret':<15} | {'Tej típus':<15} | {'Szirupok Száma':<15} | {'Hab Jelző':<15} | {'Összetevők Száma':<15} | {'Ár':<15}\n")
                for o in order.__order:
                        print(o)

        def list_dressing(dressing):

                print(f"\n{'Tétel ID':<2} | {'Rendelés ID':<2} | {'Összetvő':<15} | {'Kategória':>15} | {'Extra-e':<5}\n")
                for d in dressing.__dressing:
                        print(d)

        def list_review(review):
                
                print(f"\n{'ID':<2} | {'Értékelés ID':<15} | {'Rendelési ID':<15} | {'Várakozási idő (perc)':<15} | {'Elegedettség':>15} | {'Újrarendelné-e':<15} | {'Barista Megjegyzése':<15}\n")
                for r in review.__review:
                        print(r)               

        def run(self):
                while True:
                        print(self.MENU)
                        valasz = input("==> ")
                        match valasz:
                                case "1":
                                        
                                        self.list_order(App("data/order.csv"))
                                case "2":
                                        
                                        self.list_dressing(App("data/dressing.csv"))
                                case "3":
                                        
                                        self.list_review(App("data/review.csv"))
                                case "q":
                                        return
        
        

        
                        
                     
    