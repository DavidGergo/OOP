from csv import DictReader
from pathlib import Path
from orders import Order
from dressing import Dressing
from review import Review
from abc import ABC

import csv


def write(self, filename: str, rendelesek: list):
    
        # Meghatározzuk az oszlopneveket (pontosan úgy, ahogy a beolvasásnál volt)
        mezo_nevek = [
            "rendeles_id", "ugyfel_alias", "ital_meret", "tejtipus", 
            "szirupok_szama", "hab_jelzo", "ossz_osszetevo", "ar_ft"
        ]

        with open(filename, mode='w', encoding='utf-8-sig', newline='') as f:
            # A DictWriter-nek megadjuk a fejlécet és a pontosvesszőt
            writer = csv.DictWriter(f, fieldnames=mezo_nevek, delimiter=self.separator)

            # 1. Fejléc kiírása
            writer.writeheader()

            # 2. Adatok kiírása
            for r in rendelesek:
                # Az objektumot szótárrá alakítjuk a DictWriter számára
                writer.writerow({
                    "rendeles_id": r.rendeles_id,
                    "ugyfel_alias": r.ugyfel_alias,
                    "ital_meret": r.ital_meret,
                    "tejtipus": r.tejtipus,
                    "szirupok_szama": r.szirupok_szama,
                    "hab_jelzo": r.hab_jelzo,
                    "ossz_osszetevo": r.ossz_osszetevo,
                    "ar_ft": r.ar_ft
                })
        
        print(f"Sikeres mentés: {filename}")