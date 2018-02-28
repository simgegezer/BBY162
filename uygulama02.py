Toplamsaniye= input("saniye girin:")
print ("yıl:",int(int(Toplamsaniye)/31104000))
p= int(Toplamsaniye)%31104000
print ("ay:",int(int(p)/2592000))
r = int(p)%2592000
print ("gün:",int(int(r)/86400))
s = int(r)%86400
print ("saat:",int(int(s)/3600))
t = int(s)%3600
print ("dakika:",int(int(t)/60))
u = int(t)%60
print ("saniye:",u)