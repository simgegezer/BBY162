import tkinter
from random import choice


class Simon() :
    def __init__(self, anaSayfa):
        self.anaSayfa = anaSayfa
        self.anaSayfa.minsize(640, 480)
        self.anaSayfa.resizable(False, False)
        self.anaSayfa.title("Simon Game")
        self.anaSayfa.update()
        self.canvas = tkinter.Canvas(self.anaSayfa,width=self.anaSayfa.winfo_width(),height=self.anaSayfa.winfo_height())
        self.canvas.pack()

        self.renkler = ("red", "blue", "dark green", "yellow")
        self.acıkRenk = ("pink", "light blue", "light green", "white")
        self.parlayan = [color for color in self.renkler]
        self.dikdortgenler = []

        self.sıra = [choice(self.renkler)]
        self.sırası = 0
        self.draw_canvas()
        self.sıraGoster()

        self.anaSayfa.mainloop()

    def sıraGoster(self):
        self.yak(self.sıra[self.sırası])
        if(self.sırası < len(self.sıra) - 1):
            self.sırası += 1
            self.anaSayfa.after(1000, self.sıraGoster)
        else :
            self.sırası = 0

    def yak(self, renk):
        index = self.renkler.index(renk)
        if self.parlayan[index] == self.renkler[index] :
            self.parlayan[index] = self.acıkRenk[index]
            self.anaSayfa.after(1000, self.yak, renk)
        else :
            self.parlayan[index] = self.renkler[index]
        self.draw_canvas()


    def check_choice(self):
        dikdortgen = self.canvas.find_withtag("current")[0]
        Dikdortgen = self.dikdortgenler.index(dikdortgen)
        renk= self.renkler[Dikdortgen]
        if renk == self.sıra[self.sırası]:
            if self.sırası < len(self.sıra) - 1:
                self.sırası += 1
            else :
                self.anaSayfa.title("Simon Game - Puanınız: {}".format(len(self.sıra)))
                self.sıra.append(choice(self.renkler))
                self.sırası = 0
                self.sıraGoster()
        else :
            self.anaSayfa.title("Simon Game - Oyunu Kaybettiniz! | En Yüksek Puanınız: {}".format(len(self.sıra)))
            self.sıra[:] = []
            self.sıra.append(choice(self.renkler))
            self.sırası = 0
            self.sıraGoster()


    def draw_canvas(self):
        self.dikdortgenler[:] = []
        self.canvas.delete("all")
        for index, renk in enumerate(self.parlayan):
            if index <= 1:
                rectangle = self.canvas.create_rectangle(
                                          index * self.anaSayfa.winfo_width(),
                                          0, self.anaSayfa.winfo_width() / 2,
                                          self.anaSayfa.winfo_height() / 2,
                                          fill = renk, outline = renk)
            else:
                rectangle = self.canvas.create_rectangle(
                                        (index - 2) * self.anaSayfa.winfo_width(),
                                        self.anaSayfa.winfo_height(),
                                        self.anaSayfa.winfo_width() / 2,
                                        self.anaSayfa.winfo_height() / 2,
                                        fill = renk, outline = renk)
            self.dikdortgenler.append(rectangle)
        for id in self.dikdortgenler:
            self.canvas.tag_bind(id, '<ButtonPress-1>', lambda e : self.check_choice())


def main():
    root = tkinter.Tk()
    gui = Simon(root)


if __name__ == "__main__" : main()

