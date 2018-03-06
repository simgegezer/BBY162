__author__ = "Simge Gezer"

#Aşağıda Güneş siseminde bulunan gezegenlerden bir sözlük oluşturulmuştur. İlk fonksiyonda gezegenler ve özellikleri arasına iki nokra koyarak yazma işlemini yapmaktadır.
#İkinci fonksiyonda ise gezegenler sözlüğüne Ay uydusunu eklemektedir.
#Üçüncü de gezegenler sözlüğünün keys bölümünü vermektedir.
#Dördüncü fonksiyonda gezegenler isimli sözlüğün öğesi olan Mars'ın özelliği değiştirilmiştir.
#Beşinci de input fonksiyonu verilerek gezegen ismi girilmesi istenmiştir ve hangi gezegen adı girildiyse o gezegenin özelliğini vermektedir.
#Son fonksiyonda ise gezegenler sözlüğü silinmektedir.


gezegenler = {"Güneş": "Dünya'nın yaşam kaynağı olan Güneş orta büyüklükte bir yıldızdır",
              "Merkür": "Güneş'e en yakın, en hızlı ve Güneş sistemindeki en küçük gezegen olan Merkür adını bir Roma tanrısıdan almaktadır",
              "Venüs": "Diğer gezegenlerin tersi yönüne dönen ve Dünya ile neredeyse aynı büyüklüğe sahip olan gezegen aynı zamanda Güneş sistemindeki en sıcak gezegendir",
              "Dünya": "Güneş'e en yakın üçüncü gezegen olan Dünyamız uzaydan mavi renkte görünür ve bir uyduya sahiptir",
              "Mars": "Üzerindeki demir oksitlerinden dolayı Kızıl Gezegen olarak da bilinen Mars, Dünya gibi yıl içerisinde Güneş'e yaklaşıp uzaklaşır ve adını Roma savaş tanrısından almıştır",
              "Jüpiter": "Üzerinde fazla miktarda hidrojen ve helyum bulunduran bu gezegen Güneş etrafında dönüşünü 12 yılda tamamlar ve sistemdeki en büyük gezegendir",
              "Satürn": "Etrafında buz ve taşlardan oluşan bir halka bulunan gezegen Güneş etrafında dönüşünü yaklaşık 30 yılda tamamlar ve irili ufaklı toplam otuzdan fazla uyduya sahiptir",
              "Uranüs": "27 uydusu bu gezegen kendi etrafında dönüşünü 11 yılda, Güneş etrafındaki dönüşünü ise 84 yılda tamamlamaktadır",
              "Neptün": "Hidrojen ve helyum bakımından zengin olan gezegen Güneş'e en uzak olan gezegendir ve 14 uyduya sahiptir"}

#for i in gezegenler.items() :
    #print(i[0] + " : " + i[1])

#gezegenler["Ay"] = "Dünya'nın uydusu olan Ay insanlar tarafından ayak basılan ilk uydudur"
#print(gezegenler)

#print(gezegenler.keys())

#gezegenler={}
#gezegenler["Mars"]="İnsanlar Marrs'ın Dünya gibi yaşanabilir bir gezegen olduğunu düşündükleri için Mars'a uzay aracı göndermişlerdir"
#print(gezegenler)


print(gezegenler[input("Gezegen İsmi Giriniz: ")])

#gezegenler.clear

