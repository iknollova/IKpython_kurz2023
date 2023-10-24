#DU 4
#zadání a kontrola tel čísla, výpočet ceny sms

from math import ceil


def format_tel_cisla (tel_cislo):
    """
    Fce na overeni formatu císla
    """
    val_cislo= ()
    if len(tel_cislo) == 9:
        val_cislo = True
    elif len(tel_cislo)== 13:
            if tel_cislo[0:4] in "+420":
                val_cislo = True
            else:
                val_cislo = False
    else:
        val_cislo = False
    return val_cislo



def vyp_cena (zprava_text):
    """
    fce pro výpočet ceny text zpravy, každých 180 slov 3 Kč
    """
    cena = 3
    if len(zprava_text)>180:
         cena *= ceil(len(zprava_text)/180) 
    return cena


tel_cislo_uz = input ("Zadej telefonní číslo:")

zprava_text_uz=()
if (format_tel_cisla (tel_cislo_uz))== False:
     print(f"Zadané číslo je ve špatném formátu.")
else:
     zprava_text_uz = input ("Zadejte prosím text zprávy: ")
     print(f"Cena textové zprávy na telefonní číslo {tel_cislo_uz} je {vyp_cena(zprava_text_uz)} Kč.")  



