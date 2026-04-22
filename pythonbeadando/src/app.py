from dressing import Dressing
from review import Review
from orders import Order
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
        rekord_MENU = """
                1) Hozzáadás
                2) Törlés
                3) Módosítás
                v) Vissza
                """
        file_MENU = """
                1) Rendelések
                2) Feltétek
                3) Visszajelzések
                v) Vissza
                """
        def __init__(self):
                database = DataBase(separator=';')
                #if (filepath == "data/order.csv"):
                #        order = DataBase(separator=';')
                #        self.__order= order.rendeles_beolvas(filepath)
                #elif (filepath == "data/dressing.csv"):
                #        dre = DataBase(separator=';')
                #        self.__dressing= dre.dressing_beolvas(filepath)
                #else:
                #        rev = DataBase(separator=';')
                #       self.__review= rev.review_beolvas(filepath)
                self.__order= database.rendeles_beolvas("data/order.csv")
                self.__dressing= database.dressing_beolvas("data/dressing.csv")
                self.__review= database.review_beolvas("data/review.csv")
                
        def list_order(self):

                print(f"\n{'ID':<2} | {'Ügyfél Alias':<20} | {'Méret':<15} | {'Tej típus':<15} | {'Szirupok Száma':<15} | {'Hab Jelző':<15} | {'Összetevők Száma':<15} | {'Ár':<15}\n")
                for o in self.__order:
                        print(o)

        def list_dressing(dressing):

                print(f"\n{'Tétel ID':<2} | {'Rendelés ID':<12} | {'Összetvő':<16} | {'Kategória':<15} | {'Extra-e':<5}\n")
                for d in dressing.__dressing:
                        print(d)

        def list_review(review):
                
                print(f"\n{'Értékelés ID':<15} | {'Rendelési ID':<15} | {'Várakozási idő (perc)':<22} | {'Elegedettség':<15} | {'Újrarendelné-e':<15} | {'Barista Megjegyzése':<30}\n")
                for r in review.__review:
                        print(r)               

        def add_record(self):
                print(self.file_MENU)
                valasztott_file = input("==> ")

                database = DataBase(separator=';')

                match valasztott_file:
                        case "1":
                                print("\n\t\t ## új rendelés ##")
                                rendeles_id = max(int(o.rendeles_id) for o in self.__order) + 1
                                uj_obj = Order(
                                        str(rendeles_id), 
                                        input("Alias: "), 
                                        input("Méret: "),
                                        input("Tej: "), 
                                        input("Szirup: "),
                                        input("Hab: "),
                                        input("Össz: "), 
                                        input("Ár: ")
                                )
                                self.__order.append(uj_obj)
                                database.new_record("data/order.csv", self.__order)
                        case "2":
                                print("\n\t\t ## új feltét ##")
                                tetel_id = max(int(d.tetel_id) for d in self.__dressing) + 1
                                uj_obj = Dressing(
                                        input("Rendelés ID: "), 
                                        str(tetel_id), 
                                        input("Összetevő: "), 
                                        input("Kategória: "), 
                                        input("Extra: ")
                                )
                                self.__dressing.append(uj_obj)
                                database.new_record("data/dressing.csv", self.__dressing)
                        case "3":
                                print("\n\t\t ## új vélemény ##")
                                ertekeles_id = max(int(r.ertekeles_id) for r in self.__review) + 1
                                uj_obj = Review(
                                        str(ertekeles_id), 
                                        input("Rendeles_id: "), 
                                        input("Várakozási idő (perc): "),
                                        input("Elégedettség: "),
                                        input("Újrarendeli-e: "),
                                        input("Barista megjegyzés: ")
                                )
                                self.__review.append(uj_obj)
                                database.new_record("data/review.csv", self.__review)
                        case "v":
                                return

        def delete_record(self):
                return

        def edit_record(self):
                return
                
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
                                                        self.list_order()
                                                case "2":
                                                        self.list_dressing()
                                                case "3":
                                                        self.list_review()
                                                case "v":
                                                        continue
                                case "2":
                                        print(self.rekord_MENU)
                                        rekord_valasz = input("==> ")
                                        match rekord_valasz:
                                                case "1": 
                                                        self.add_record()
                                                case "2":
                                                        self.delete_record()
                                                case "3":
                                                        self.edit_record()
                                                case "v":
                                                        continue
                                case "3":
                                        #Keresés
                                        return
                                case "q":
                                        return
        
        

        
                        
                     
    