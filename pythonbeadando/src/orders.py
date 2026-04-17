from dataclasses import dataclass

@dataclass
class Order():
    def __init__(self, rendeles_id, ugyfel_alias, ital_meret, tejtipus, szirupok_szama, hab_jelzo, ossz_osszetevo, ar_ft):
        self.rendeles_id = rendeles_id
        self.ugyfel_alias = ugyfel_alias
        self.ital_meret = ital_meret
        self.tejtipus = tejtipus
        self.szirupok_szama = szirupok_szama
        self.hab_jelzo = hab_jelzo
        self.ossz_osszetevo = ossz_osszetevo
        self.ar_ft = ar_ft
    
    def __str__(self):
        # A számok (pl. 5, 20, 10) határozzák meg az oszlopok szélességét
        # A < jel balra, a > jel jobbra igazít
        return (f"{self.rendeles_id:<2} | "
                f"{self.ugyfel_alias:<20} | "
                f"{self.ital_meret:<15} | "
                f"{self.tejtipus:<15} | "
                f"{self.szirupok_szama:<15} | "
                f"{self.hab_jelzo:<15} | "
                f"{self.ossz_osszetevo:<16} | "
                f"{self.ar_ft:<5} Ft")
