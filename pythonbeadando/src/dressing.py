from dataclasses import dataclass

@dataclass
class Dressing():

    def __init__(self, tetel_id, rendeles_id, osszetevo, kategori, extra):
        self.rendeles_id = rendeles_id
        self.tetel_id = tetel_id
        self.osszetevo = osszetevo
        self.kategori = kategori
        self.extra = extra

    
    def __str__(self):
        # A számok (pl. 5, 20, 10) határozzák meg az oszlopok szélességét
        # A < jel balra, a > jel jobbra igazít
        return (f"{self.rendeles_id:<8} | "
                f"{self.tetel_id:<12} | "     
                f"{self.osszetevo:<16} | "
                f"{self.kategori:<15} | "
                f"{self.extra:5}")
