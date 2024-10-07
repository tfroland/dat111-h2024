#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:18:34 2024

@author: tord
"""

# Karaktervariabler
navnPaaKarakter = input("Hva er navnet på karakteren?\n")
gull = 100

inventar = []

# Butikkvariabler
varelager = [("Sverd", 20), ("Stav", 70), ("Kappe", 25)]

# Gir utskrift til brukeren for å starte karakterskaperen
print("\nDu skal nå kjøpe startutstyr fra butikken.")
print("Butikken består av følgende varer:")
teller = 1
for vare in varelager:
    print("Vare " + str(teller) + ": " + vare[0] + ", verdi: " + str(vare[1]))
    teller += 1

antallVarerAaKjøpe = input("\nHvor mange varer ønsker du å kjøpe? ")

# Håndterer kjøp av første utstyr
for x in range(int(antallVarerAaKjøpe)):
    oensketVarenummer = int(input("Hvilket varenummer ønsker du å kjøpe (1-3)? "))
    if(gull >= varelager[oensketVarenummer - 1][1]):
        inventar.append(varelager[oensketVarenummer - 1])
        gull -= varelager[oensketVarenummer - 1][1]
    else:
        print("Ukjent vare, eller ikke råd til vare. Ingenting ble kjøpt.")
    

# Gir en utskrift av karakterinfo
print("\nKarakteren er nå ferdigskapt og har følgende detaljer:")
print("Navn: " + navnPaaKarakter);
teller = 1
for utstyr in inventar:
    print("Utstyr " + str(teller) + ": " + utstyr[0] + ", med verdi " + str(utstyr[1]))
    teller += 1