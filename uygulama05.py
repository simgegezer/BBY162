__author__ = "Simge Gezer"

import random
şehirler = random.choice(['tekirdağ', 'bilecik', 'artvin', 'istanbul', 'kars', 'diyarbakır', 'izmir', 'yalova', 'çanakkale', 'gaziantep','konya', 'ankara', 'antalya', 'kocaeli', 'samsun', 'denizli', 'kahramanmaraş'])
kelime = []
can = 6
boşluk = '_'

kelimeçizgisi = list(boşluk * len(şehirler))

dongu = 1

while dongu:
    print(' '.join(kelimeçizgisi), end='\n\n')

    seçilenharf= input('Harf Giriniz: ').lower()

    try:
        int(seçilenharf)
        print('Lütfen bir harf giriniz.\n')
    except:
        if len(seçilenharf) > 1:
            print('HARF giriniz!\n')
        else:
            if seçilenharf in kelime:
                print('Bu harfi zaten girdiniz.\n')
            else:
                doğru = None
                for i in range(len(şehirler)):
                    if seçilenharf == şehirler[i]:
                        doğru = True

                        kelimeçizgisi[i] = seçilenharf

                        kelime.append(seçilenharf)

                        if boşluk not in kelimeçizgisi:
                            print(' '.join(kelimeçizgisi))
                            print('\nTebrikler oyunu kazandınız')

                            dongu = 0

                else:

                    if doğru != True:
                        can -= 1

                        print('Yanlış harf. Kalan hakkınız: {}\n'.format(can))

                kelime.append(seçilenharf)


                if can == 0:
                    print(' Oyunu Kaybettiniz. Seçilen kelime "{}" idi.\n'.format(şehirler))

                    break


