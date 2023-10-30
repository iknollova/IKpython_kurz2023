#DU5 = totéž, co cvičení v hodině

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prum_teplota = [sum(teplota)/ len(teplota) for teplota in teploty]
ranni_teplota = [teplota[0] for teplota in teploty]
nocni_teplota = [teplota[-1] for teplota in teploty]
pol_noc_teplota =[ [teplota[1], teplota[-1]] for teplota in teploty]

print(prum_teplota)
print(ranni_teplota)
print(nocni_teplota)
print(pol_noc_teplota)


# bonus

teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]



#vytvoření slovníku s průměrnými hodnotami bez Dictionary comprehension
teplota_s={}
for teplota in teploty:
    teplota_s.update({teplota[0]:(sum(teplota[1:5])/len(teplota[1:5]))})

print(teplota_s)

#S pomocí Dictionary comprehension
#1krok -vytvoření nejdříve dictionary s dnem (klíč) a teplotami (seznam 4 hodnot)
teplota1 = {}
for teplota in teploty:
    teplota1.update({teplota[0]: teplota[1:5]})
    

#2krok pak pomocí dictionary comprehension vytvoření slovníku - den(klíč) a prům teplota (hodnota)
teplota_dict= {den:sum(tepl)/len(tepl) for (den, tepl) in teplota1.items()}

print(teplota_dict)

#pokoušela jsem se dát 1 a 2 krok dohromady, ale nepovedlo 