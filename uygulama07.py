
from tkinter import *
from PIL import Image, ImageTk
album = Tk()
album.title("Resim Albümü")


resim1 = ImageTk.PhotoImage(Image.open("resim1.jpg"))
resim2 = ImageTk.PhotoImage(Image.open("resim2.jpg"))

etiket = Label(album, text="Resim Albümü")
etiket.pack()

def ileri():
    if display == resim1:
        panel1.configure(image=resim2)
    else:
        panel1.configure(image=resim1)

ileributon = Button(album, text="İleri", command=ileri)
ileributon.pack(side="right")

def geri():
    if display2 == resim2:
        panel1.configure(image = resim1)
    else:
        panel1.configure(image = resim2)

geributon = Button(album, text="Geri", command=geri)
geributon.pack(side="left")

panel1 = Label(album, image=resim1)
display = resim1
panel1.pack(side="top")

panel2 = Label(album, image=resim2)
display2 = resim2


album.mainloop()


