from dressing import Dressing
from review import Review
from orders import Order
from csv_reader import DataBase
from statistic import Statistics

class App():
        MENU = """
                1) Kilistázások
                2) Rekordok kezelése
                3) Keresések
                4) Statisztika
                q) quit
                """
        Lista_MENU = """
                1) Rendelések
                2) Feltétek
                3) Vélemények
                q) vissza
                """
        rekord_MENU = """
                1) Hozzáadás
                2) Törlés
                3) Módosítás
                q) Vissza
                """
        file_MENU = """
                1) Rendelések
                2) Feltétek
                3) Visszajelzések
                q) Vissza
                """
        def __init__(self):
                self.database = DataBase(separator=';')
                self.__order= self.database.rendeles_beolvas("data/order.csv")
                self.__dressing= self.database.dressing_beolvas("data/dressing.csv")
                self.__review= self.database.review_beolvas("data/review.csv")
                
        def list_order(self):

                print(f"\n{'ID':<2} | {'Ügyfél Alias':<20} | {'Méret':<15} | {'Tej típus':<15} | {'Szirupok Száma':<15} | {'Hab Jelző':<15} | {'Összetevők Száma':<15} | {'Ár':<15}\n")
                for o in self.__order:
                        print(o)

        def list_dressing(self):

                print(f"\n{'Tétel ID':<2} | {'Rendelés ID':<12} | {'Összetvő':<16} | {'Kategória':<15} | {'Extra-e':<5}\n")
                for d in self.__dressing:
                        print(d)

        def list_review(self):
                
                print(f"\n{'Értékelés ID':<15} | {'Rendelési ID':<15} | {'Várakozási idő (perc)':<22} | {'Elegedettség':<15} | {'Újrarendelné-e':<15} | {'Barista Megjegyzése':<30}\n")
                for r in self.__review:
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
                        case "q":
                                return

        def delete_record(self):
                print("\n"+"="*20 + "  Rekord Törlés  " + "="*20)
                print("\n\t Rendelések: ")
                self.list_order()
                print("\n\t Feltétek: ")
                self.list_dressing()
                print("\n\t Vélemények: ")
                self.list_review()
                print("\n")
                ToDelete = input("Add meg a törölni klvánt elem rendelési ID-át: ")

                order_found = False
                for i in range(len(self.__order)):
                        if str(self.__order[i].rendeles_id).strip() == ToDelete:
                                del self.__order[i]
                                order_found = True
                                break
                
                for i in range(len(self.__dressing)):
                        if str(self.__dressing[i].rendeles_id).strip() == ToDelete:
                                del self.__dressing[i]
                                break
                
                for i in range(len(self.__review)):
                        if str(self.__review[i].rendeles_id).strip() == ToDelete:
                                del self.__review[i]
                                break
                
                if order_found:
                        self.database.new_record("data/order.csv", self.__order)
                        self.database.new_record("data/dressing.csv", self.__dressing)
                        self.database.new_record("data/review.csv", self.__review)

                        print("\n\t Rendelés törölve")
                        print("\n\t Rendelések: ")
                        self.list_order()
                        print("\n\t Feltétek: ")
                        self.list_dressing()
                        print("\n\t Vélemények: ")
                        self.list_review()

        def edit_record(self):
                while True:
                        print("\n" + "="*15 + " Módosítás " + "="*15) 
                        print(self.file_MENU)
                        chosen_file = input("Melyik file-ban akarsz dolgozni? : ")

                        if chosen_file.lower() == "q":
                                break

                        file = None
                        file_path = ""
                        search = "rendeles_id"

                        if chosen_file == "1":
                                file = self.__order
                                file_path = "data/order.csv"
                                self.list_order()
                        elif chosen_file == "2":
                                file = self.__dressing
                                file_path = "data/dressing.csv"
                                self.list_dressing()
                        elif chosen_file == "3":
                                file = self.__review
                                file_path = "data/review.csv"
                                self.list_review()
                        else:
                                print("\nHIBA: Ilyen file szám nincs! \n")
                                continue
                        
                        
                        target_id = input("Add meg a rendelés ID-t: ")

                        found = None
                        for elem in file:
                                if str(getattr(elem, search)).strip() == target_id:
                                        found = elem
                                        break
                        if not found:
                                print("\nHIBA: Nincs ilyen ID!\n")
                                continue
                        
                        available = list(found.to_dict().keys())
                        print(f"\nELérhető mezők: {' , '.join(available)}")
                        field = input("\nMelyik mezőn szeretnél módosítani? : ")
                        if field not in field:
                                print("\n HIBA: Nincs ilyen mezőnév!\n")
                                continue

                        current_value = getattr(found, field)
                        print(f"\n Jelenlegi érték: {field} : {current_value}")
                        new_val = input(f"Add meg az új értékét:\t {field} : ")

                        setattr(found, field, new_val)
                        self.database.new_record(file_path, file)

        def search_by_size(self):
                size = input("Melyik méretre vagy kíváncsi? (kicsi:1 - 3:nagy) : ")

                found = []
                match size:
                        case "1":
                                self.search_output("kicsi")
                        case "2":
                                self.search_output("közepes")
                        case "3":
                                self.search_output("nagy")

        def search_output(self, size):
                found_anything = False # Hogy tudjuk, volt-e egyáltalán találat
        
                for o in self.__order:
                        if str(o.ital_meret).strip().lower() == size.strip().lower():
                                found_anything = True
                                found_index = o.rendeles_id
                                print("\n"*2)
                                # 1. Rendelés adatainak kiírása
                                print(f"RENDELÉS [{found_index}] | Ügyfél: {o.ugyfel_alias} | Méret: {o.ital_meret} | Tej: {o.tejtipus}\n")
                                
                                # 2. Belső ciklus a feltéteknek
                                print("Feltétek:")
                                dressing_found = False
                                for d in self.__dressing:
                                        if str(d.rendeles_id).strip() == str(found_index).strip():
                                                print(f"\t-> {d.osszetevo} ({d.kategori})\n")
                                                dressing_found = True
                                if not dressing_found:
                                        print("\t(Nincsenek feltétek)")

                                # 3. Belső ciklus a véleményeknek
                                print("\nVélemények:")
                                review_found = False
                                for r in self.__review:
                                        if str(r.rendeles_id).strip() == str(found_index).strip():
                                                print(f"\t Várakozás: {r.varakozasi_ido_perc} perc | Elégedettség: {r.elegedettseg}/10\n")
                                                review_found = True
                                if not review_found:
                                        print("\t(Nincs értékelés)")
                                

                                if not found_anything:
                                        print(f"\nHIBA: Nincs '{size}' méretű rendelés a rendszerben!\n")

        def show_stats(self):
                stat = Statistics(self.__order, self.__dressing, self.__review)
                stat.show_all_stat()

        def run(self):
                while True:
                        print("\n"+"="*20 + "  +++  " + "="*20)
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
                                        self.search_by_size()
                                case "4":
                                        self.show_stats()

                                case "q":
                                        return
        
        

        
                        
                     
    