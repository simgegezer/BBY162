__author__ = "Simge Gezer"

import random

sehirler = random.choice(['tekirdağ', 'bilecik', 'artvin', 'istanbul', 'kars', 'diyarbakır', 'izmir', 'yalova', 'çanakkale', 'gaziantep',])
canSayı= 4
adamAsmaca = []
bosluk = "_"

print("A D A M  A S M A C A\n")

for kelime in sehirler:

    adamAsmaca.append(bosluk)

print(adamAsmaca)

while canSayı > 0:

    i = 0

    girdi = input("\nBir harf giriniz: ").lower()

    if girdi in sehirler:
        for kontrol in sehirler:
            if sehirler[i] == girdi:
                adamAsmaca[i] = girdi
            i += 1

        print("")
        print(adamAsmaca)

    else:
        canSayı -= 1
        print("")
        print(adamAsmaca)
        print("Kalan can sayısı = " + str(canSayı))

    if canSayı == 0:
        print('Oyunu kaybettiniz! Seçilen kelime "{}" idi.\n'.format(sehirler))
        break

    if bosluk not in adamAsmaca:
        print("\nTebrikler! Doğru kelimeyi buldunuz!")
        break

