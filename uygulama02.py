Toplamsaniye= input("saniye girin:")
print ("yıl:",int(int(Toplamsaniye)/93313200))
p= int(Toplamsaniye)%93313200
print ("ay:",int(int(p)/7776000))
r = int(p)%7776000
print ("gün:",int(int(r)/259200))
s = int(r)%259200
print ("saat:",int(int(s)/10800))
t = int(s)%10800
print ("dakika:",int(int(t)/180))
u = int(t)%180
print ("saniye:",u)