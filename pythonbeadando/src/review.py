from dataclasses import dataclass

@dataclass
class Review():
    def __init__(self,ertekeles_id , rendeles_id, varakozasi_ido_perc, elegedettseg, ujrarende, barista):
        self.rendeles_id = rendeles_id
        self.ertekeles_id = ertekeles_id
        self.varakozasi_ido_perc = varakozasi_ido_perc
        self.elegedettseg = elegedettseg
        self.ujrarendeli_e = ujrarende
        self.barista_megjegyzes = barista
    
    def __str__(self):
        # A számok (pl. 5, 20, 10) határozzák meg az oszlopok szélességét
        # A < jel balra, a > jel jobbra igazít
        return (f"{self.ertekeles_id:15} | "
                f"{self.rendeles_id:<15} | "
                f"{self.varakozasi_ido_perc:<22} | "
                f"{self.elegedettseg:<15} | "
                f"{self.ujrarendeli_e:<15} | "
                f"{self.barista_megjegyzes:<30}")

    def to_dict(self):
        return {
            "ertekeles_id":self.ertekeles_id,
            "rendeles_id":self.rendeles_id,
            "varakozasi_ido_perc": self.varakozasi_ido_perc,
            "elegedettseg_1_10":self.elegedettseg,
            "ujrarendeli_e":self.ujrarendeli_e,
            "barista_megjegyzes":self.barista_megjegyzes
        }