__author__ = "Simge GEZER"

isim=input("Erkek İsmi Giriniz..:")
isim1=input("Kadın İsmi Giriniz..:")
mısra=input("1 ve 8 Arasında Mısra Sayısı Giriniz..:")
sec=int(mısra)
boşluk=" "
baglac= "ile"
yer=["sınıfta", "metroda", "yolda", "evde", "parkta", "salonda", "müzede", "bahçede", "arabada", "balkonda" ]
fiil=["güldü", "yemek pişirdi", "yemeğe tuz attı", "çöpü attı", "şarkı söyledi", "bağırdı", "eşyalarını taşıdı", "yerleri sildi","konuştu", "ayakkabı satın aldı"]

import random
def kelime2():
    secim = random.choice(yer)
    yer.remove(secim)
    return secim
def kelime3():
    secim = random.choice(fiil)
    fiil.remove(secim)
    return secim

a=(isim+boşluk+baglac+boşluk+kelime2()+boşluk+isim1+boşluk+kelime3()+"\n")
b=(isim+boşluk+baglac+boşluk+kelime2()+boşluk+isim1+boşluk+kelime3()+"\n")
c=(isim+boşluk+baglac+boşluk+kelime2()+boşluk+isim1+boşluk+kelime3()+"\n")
d=(isim+boşluk+baglac+boşluk+kelime2()+boşluk+isim1+boşluk+kelime3()+"\n")
e=("\n")
f=(isim+boşluk+baglac+boşluk+kelime2()+boşluk+isim1+boşluk+kelime3()+"\n")
g=(isim+boşluk+baglac+boşluk+kelime2()+boşluk+isim1+boşluk+kelime3()+"\n")
h=(isim+boşluk+baglac+boşluk+kelime2()+boşluk+isim1+boşluk+kelime3()+"\n")
ı=(isim+boşluk+baglac+boşluk+kelime2()+boşluk+isim1+boşluk+kelime3()+"\n")

while True:
    if sec==1:
        print(e,a)
        print

    elif sec==2:
        print(e,a,b)
        print

    elif sec==3:
        print(e,a,b,c)
        print

    elif sec==4:
        print(e,a,b,c,d)
        print

    elif sec==5:
        print(e,a,b,c,d,e,f)
        print

    elif sec==6:
        print(e,a,b,c,d,e,f,g)
        print

    elif sec==7:
        print(e,a,b,c,d,e,f,g,h)
        print

    elif sec==8:
        print(e,a,b,c,d,e,f,g,h,ı)
        print



    else:
        print("Mısra sayısı geçildi....")
    break










