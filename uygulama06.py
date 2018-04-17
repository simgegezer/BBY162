_author_="Simge Gezer"

import random
from tkinter import Tk, Label, Button

class yemekListem:
    def __init__(self, anaSayfa):
        self.anaSayfa= anaSayfa
        anaSayfa.title=("Günün Yemeği")
        anaSayfa.configure(background="light blue")

        self.label= Label(anaSayfa, text="Bugünün Yemeği",font=("Arial",12),bg="light blue")
        self.label.pack()

        self.yemek_button= Button(anaSayfa, text="Merhabalar",font=("Algerian",11), command= self.yemek,bg="pink")
        self.yemek_button.pack()

        self.gununYemeginiSec= Button(anaSayfa, text="Günün Yemeğini Göster",font=("Book Antiqua",11),command=self.gununYemegi,bg="purple")
        self.gununYemeginiSec.pack()

        self.cıkıs=Button(anaSayfa, text="Kapat",font=("Copperplate Gothic Light",11),command= anaSayfa.quit,bg="brown")
        self.cıkıs.pack()

    def yemek(self):
        print("Merhabalar!!!")

    def gununYemegi(self):
        yemekler=("Mercimek Çorbası-Nohutlu Taze Bakla-Salata","Ezogelin Çorba-Taze Barbunya Köftesi-Cacık", "Yayla Çorbası-Domatesli Makarna-Salata", "Domates Çorbası-Mantar Yemeği-Sütlaç","Mantar Çorbası-Fırında Tavuk Şiş-Baklava","Patates Çorbası-Pırasa Yemeği-Dondurma","Terbiyeli Tavuk Çorbası-Levrek Buğulama-Şekerpare","Sebze Çorbası-Kereviz Yemeği-Salata","Yoğurt Çorbası-Kıymalı Semizotu-İrmik Helvası","Pirinç Çorbası-Kuru Fasulye-Turşu")
        secilenYemek=random.choice(yemekler)
        self.yemeklerim= Label(self.anaSayfa, text=secilenYemek)
        self.yemeklerim.pack()

root=Tk()
listem=yemekListem(root)
root.mainloop()