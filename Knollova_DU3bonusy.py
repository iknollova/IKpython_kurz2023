import json
#ukol
with open('body.json', mode='r', encoding='utf-8' ) as file:
    data = json.load(file)

print(data)

vysledky = {}
for jmena,body in data.items():
    if body >= 60:
        vysledky[jmena]= "Pass"
    else:
        vysledky[jmena]= "Fail"
print(vysledky)

with open("prospech.json", mode="w", encoding="utf-8") as output_file:
    json.dump(vysledky, output_file)

#bonus  
with open('body.json', mode='r', encoding='utf-8' ) as file:
    vysledky = json.load(file)
with open('bonusy.json', mode='r', encoding='utf-8' ) as file:
    bonusy = json.load(file)

print(vysledky)
print(bonusy)


for name, bonus in bonusy.items():
    if name in vysledky:
        vysledky[name]+=bonus
    


znamka = {}
for jmeno, body in vysledky.items():
    if body >= 90:
        znamka[jmeno]= 1
    elif body >= 70 and body<90:
        znamka[jmeno]= 2
    elif body >= 50 and body<70:
        znamka[jmeno]= 3
    elif body >= 30 and body<50:
        znamka[jmeno]= 4
    else:
        znamka[jmeno]= 5

print(znamka)
    
with open("znamka.json", mode="w", encoding="utf-8") as output_file:
    json.dump(znamka, output_file)

