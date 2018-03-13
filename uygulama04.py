__author__= "Simge GEZER"


erkekadı = input("Bir erkek ismi giriniz:  ")
kadınadı = input("Bir kadın ismi giriniz:  ")
dize = int(input("Dize sayısı giriniz...Maksimum 12 mısra yazdırılabilir..  "))



sarkı = [erkekadı + " " "Ağlamak için gözden yaş mı akmalı?  " , "Dudaklar gülerken insan ağlayamaz mı? " + kadınadı + " " "Sevmek için güzele mi bakmalı? " ,"Çirkin bir tende ruh, kalbi bağlayamaz mı?" + erkekadı + " " "Hasret; özlenenden uzak mı kalmaktır?", " Özlenen yakındayken hicran duyulmaz mı? " + kadınadı + " " " Hırsızlık; para, mal mı çalmaktır?" , "Saadet çalmak hırsızlık olamaz mı?"  +  erkekadı  + " " "Solması için gülü dalından mı koparmalı?" , "Pembe bir gonca iken dalında solamaz mı?"  + kadınadı + " " "Öldürmek için silah, hançer mi olmalı? " , "Saçlar bağ, gözler silah, gülüş kurşun olamaz mı?"]

for olusturulacak_sarkı in sarkı[:dize]:
    print(olusturulacak_sarkı)

if dize > 12:
    print("En az 12 adet dize giriniz...")


