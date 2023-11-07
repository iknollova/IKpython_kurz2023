class Auto:
    def __init__(self,registracni_znacka, typ_vozidla,najete_km,dostupne ) :
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne=False
            return f"Potvrzuji zapůjčení vozidla."
            
        else:
            return f"Vozidlo není k dispozici."
    def get_info(self):
        return f"Vozidlo: {self.typ_vozidla}, RZ: {self.registracni_znacka}."


  
    
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253, True)

# print(auto1.get_info())
# print(auto2.get_info())


   

def pujceni (auto):
    if auto_uz == "Pegueot":
        print(auto1.get_info())
        print(auto1.pujc_auto()) 
    elif auto_uz == "Škoda":
        print(auto2.get_info())
        print(auto2.pujc_auto())
    else:
        print (f"Vozidlo {auto_uz} nemáme v nabídce půjčovny.")

auto_uz = input("Jaký typ vozidla si chcete půjčit (Škoda, Pegueot): ")
pujceni(auto_uz)
#zavolání podruhé, otestování aby nešlo auto podruhé půjčit, protože při novém spuštění se hodnota dostupné resetuje na TRUE
auto_uz = input("Jaký typ vozidla si chcete půjčit (Škoda, Pegueot): ")
pujceni(auto_uz)


