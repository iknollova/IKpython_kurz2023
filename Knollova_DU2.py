#SKLAD

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = input ("Kód součástky: ")

if soucastka not in sklad:
    print (f"Vámi zadaná součástka s kódem {soucastka} není na skladě.")
else:
    mnozstvi = int(input ("Napište požadované množství množství: "))
    if mnozstvi > sklad[soucastka]:
        print (f"Na skladě je pouze {sklad[soucastka]} ks. Expedujeme {sklad[soucastka]} ks.")
        sklad.pop (soucastka)
    elif mnozstvi == sklad[soucastka]:
        print (f"Součástka je na skladě v dostatečném množství. Expedujeme Vámi požadovaných {mnozstvi} ks.")
        sklad.pop(soucastka)
    else:
        print (f"Součástka je na skladě v dostatečném množství. Expedujeme Vámi požadovaných {mnozstvi} ks.")
        sklad[soucastka] -= mnozstvi

#print(sklad)




