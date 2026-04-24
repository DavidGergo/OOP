
class Statistics:
    def __init__(self, orders, dressings, reviews):
        # Megkapja az App osztálytól a már beolvasott listákat
        self.orders = orders
        self.dressings = dressings
        self.reviews = reviews

    def show_all_stat(self):
        print("\t"+"="*20 + "  Statiszika  " + "="*20)
        self.income_by_size()
        self.top_dressing()
        self.extra_ratio()
        self.avr_satistfaction()
        self.alternative_milk()


    def income_by_size(self):
        rendelesek_szama = len(self.orders)
        osszes_bevetel = 0
        stats = {}
        
        for o in self.orders:
            m = str(o.ital_meret).strip().lower()
            try:
                ar_tiszta = "".join(filter(str.isdigit, str(o.ar_ft)))
                ar_szam = int(ar_tiszta) if ar_tiszta else 0
            except (ValueError, TypeError):
                ar_szam = 0
            
            if m not in stats:
                stats[m] = 0
            
            stats[m] += ar_szam
            osszes_bevetel += ar_szam
        
        print("\n\t Bevétel méretenként:")
        if not stats:
            print("\t\t Nincs beolvasott adat.")
        else:
            for m, osszeg in stats.items():
                # Formázott kiírás ezres elválasztóval
                print(f"\t\t {m.capitalize():<10}: {osszeg:>7} Ft")
        
        if rendelesek_szama > 0:
            atlag_ar = osszes_bevetel / rendelesek_szama
            print(f"\n\tÖsszes bevétel:      {osszes_bevetel:,} Ft")
            print(f"\tÁtlagos kosárérték:  {atlag_ar:,.0f} Ft")
        else:
            print("\n    Nincs adat az átlag számításához.")

    def top_dressing(self):
        counts = {}
        for d in self.dressings:
            nev = d.osszetevo.strip()
            counts[nev] = counts.get(nev, 0) + 1

        rendezheto_lista = []
        for nev, db in counts.items():
            rendezheto_lista.append((db, nev))

        rendezheto_lista.sort(reverse=True)

        print("\n\tTop 5 legnépszerűbb feltét:")
        for db, nev in rendezheto_lista[:5]:
            print(f"\t\t {nev:<15}: {db} alkalom")

    def extra_ratio(self):
        if not self.dressings: return
        extrak = [d for d in self.dressings if d.extra.lower() == "igen"]
        szazalek = (len(extrak) / len(self.dressings)) * 100
        
        print("\n\tExtra igények aránya:")
        print(f"\t\t A feltétek {szazalek:.1f}%-a extra kérés.")

    def avr_satistfaction(self):
        if not self.reviews:
            print("\n Nincs elég vélemény az átlagoláshoz.")
            return
            
        osszes_pont = sum(int(r.elegedettseg) for r in self.reviews)
        osszes_ido = sum(int(r.varakozasi_ido_perc) for r in self.reviews)
        atlag_pont = osszes_pont / len(self.reviews)
        atlag_ido = osszes_ido / len(self.reviews)
        
        print("\n\tVásárlói visszajelzések átlaga:")
        print(f"\t\t Elégedettség: {atlag_pont:.1f} / 10")
        print(f"\t\t Várakozási idő: {atlag_ido:.1f} perc")

    def alternative_milk(self):
        alternativ = [o for o in self.orders if o.tejtipus.lower() not in ["normál", "tehén", "nincs"]]
        szazalek = (len(alternativ) / len(self.orders)) * 100 if self.orders else 0
        
        print("\n\tTejmentes/Alternatív igények:")
        print(f"\t\t A rendelések {szazalek:.1f}%-a speciális tejjel készült.")