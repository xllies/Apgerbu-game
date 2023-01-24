from tkinter import *
import random

GARUMS = 558
PLATUMS = 864
logs = Tk()
logs.title('Ko vilkt?')

c = Canvas(logs, width=PLATUMS, height=GARUMS, bg='#4b6fa6') 
c.pack()


# MAN ON CLOTHES---------------------------------------------------


class Game:
    def __init__(self):
        button_start = PhotoImage(file = 'pictures/start-button.png')
        bg_start = PhotoImage(file = 'pictures/home-bg.png')
        bg_choose = PhotoImage(file = 'pictures/choose-lvl.png')
        bg_gender = PhotoImage(file = 'pictures/gender-bg.png')
        bg_wedding = PhotoImage(file = 'pictures/wedding-bg.png')
        bg_school = PhotoImage(file = 'pictures/bg_school.png')
        bg_beach = PhotoImage(file = 'pictures/beach-bg.png')
        bg_party = PhotoImage(file = 'pictures/party-bg.png')
        bg_buizness = PhotoImage(file = 'pictures/wedding-bg.png')

        poga_woman = PhotoImage(file = 'pictures/poga-woman.png')
        poga_man = PhotoImage(file = 'pictures/poga-man.png')
        poga_rand = PhotoImage(file = 'pictures/poga-rand.png')

        baloon1 = PhotoImage(file = 'pictures/baloon-wedding.png')
        baloon2 = PhotoImage(file = 'pictures/baloon-school.png')
        baloon3 = PhotoImage(file = 'pictures/baloon-beach.png')
        baloon4 = PhotoImage(file = 'pictures/baloon-party.png')
        baloon5 = PhotoImage(file = 'pictures/baloon-buizness.png')

        on_man_top1 = PhotoImage(file = 'pictures/man-clothes/top1.png')
        on_man_top2 = PhotoImage(file = 'pictures/man-clothes/top2.png')
        on_man_top3 = PhotoImage(file = 'pictures/man-clothes/top3.png')
        on_man_top4 = PhotoImage(file = 'pictures/man-clothes/top4.png')
        on_man_top5 = PhotoImage(file = 'pictures/man-clothes/top5.png')

        on_man_bot1 = PhotoImage(file = 'pictures/man-clothes/bot1.png')
        on_man_bot2 = PhotoImage(file = 'pictures/man-clothes/bot2.png')
        on_man_bot3 = PhotoImage(file = 'pictures/man-clothes/bot3.png')
        on_man_bot4 = PhotoImage(file = 'pictures/man-clothes/bot4.png')
        on_man_bot5 = PhotoImage(file = 'pictures/man-clothes/bot5.png')

        on_man_socks1 = PhotoImage(file = 'pictures/man-clothes/socks1.png')
        on_man_socks2 = PhotoImage(file = 'pictures/man-clothes/socks2.png')

        on_man_pair1 = PhotoImage(file = 'pictures/man-clothes/pair1.png')
        on_man_pair2 = PhotoImage(file = 'pictures/man-clothes/pair2.png')
        on_man_pair3 = PhotoImage(file = 'pictures/man-clothes/pair3.png')
        on_man_pair4 = PhotoImage(file = 'pictures/man-clothes/pair4.png')


        self.bg_start = bg_start
        self.button_start = button_start
        self.bg_choose = bg_choose
        self.bg_gender = bg_gender
        self.bg_wedding = bg_wedding
        self.bg_school = bg_school
        self.bg_beach = bg_beach
        self.bg_party = bg_party
        self.bg_buizness = bg_buizness

        self.poga_woman = poga_woman
        self.poga_man = poga_man
        self.poga_rand = poga_rand

        self.baloon1 = baloon1
        self.baloon2 = baloon2
        self.baloon3 = baloon3
        self.baloon4 = baloon4
        self.baloon5 = baloon5


        self.on_man_top1 = on_man_top1
        self.on_man_top2 = on_man_top2
        self.on_man_top3 = on_man_top3
        self.on_man_top4 = on_man_top4
        self.on_man_top5 = on_man_top5

        self.on_man_bot1 = on_man_bot1
        self.on_man_bot2 = on_man_bot2
        self.on_man_bot3 = on_man_bot3
        self.on_man_bot4 = on_man_bot4
        self.on_man_bot5 = on_man_bot5

        self.on_man_socks1 = on_man_socks1
        self.on_man_socks2 = on_man_socks2

        self.on_man_pair1 = on_man_pair1
        self.on_man_pair2 = on_man_pair2
        self.on_man_pair3 = on_man_pair3
        self.on_man_pair4 = on_man_pair4

        Game.open_all(self)

    def open_all(self):
        
        self.fons = c.create_image(432,279, image = self.bg_start)
        self.start_poga = Button(c,image=self.button_start, command=lambda:Game.choose_level(self),background='#6B4531', activebackground='#6B4531', bd=0)
        self.start_poga.place(x=244,y=180)

    def choose_level(self):
        c.delete('all')
        self.start_poga.destroy()

        self.baloon_btn1 = Button(c,image=self.baloon1, command=lambda:Game.gender(self, 'wedding'),background='#79C9F9', activebackground='#79C9F9', bd=0)
        self.baloon_btn1.place(x=43,y=83)
        self.baloon_btn2 = Button(c,image=self.baloon2, command=lambda:Game.gender(self, 'school'),background='#79C9F9', activebackground='#79C9F9', bd=0)
        self.baloon_btn2.place(x=188,y=5)
        self.baloon_btn3 = Button(c,image=self.baloon3, command=lambda:Game.gender(self, 'beach'),background='#79C9F9', activebackground='#79C9F9', bd=0)
        self.baloon_btn3.place(x=362,y=116)
        self.baloon_btn4 = Button(c,image=self.baloon4, command=lambda:Game.gender(self, 'party'),background='#79C9F9', activebackground='#79C9F9', bd=0)
        self.baloon_btn4.place(x=533,y=14)
        self.baloon_btn5 = Button(c,image=self.baloon5, command=lambda:Game.gender(self, 'buisness'),background='#79C9F9', activebackground='#79C9F9', bd=0)
        self.baloon_btn5.place(x=688,y=116)

        
        self.fons = c.create_image(432,279, image = self.bg_choose)



    def gender(self, theme):
        c.delete('all')
        self.baloon_btn1.destroy()
        self.baloon_btn2.destroy()
        self.baloon_btn3.destroy()
        self.baloon_btn4.destroy()
        self.baloon_btn5.destroy()

        self.theme = theme

        self.fons = c.create_image(432,279, image = self.bg_gender)

        self.poga1 = Button(c,image=self.poga_woman, command=lambda:Game.level_start(self, 0),background='#7FAD71', activebackground='#7FAD71', bd=0)
        self.poga1.place(x=65,y=475)

        self.poga2 = Button(c,image=self.poga_man, command=lambda:Game.level_start(self, 1),background='#7FAD71', activebackground='#7FAD71', bd=0)
        self.poga2.place(x=338,y=475)

        self.poga3 = Button(c,image=self.poga_rand, command=lambda:Game.level_start(self, random.randint(0,1)),background='#7FAD71', activebackground='#7FAD71', bd=0)
        self.poga3.place(x=600,y=475)


    def level_start(self, gender):
        self.poga1.destroy()
        self.poga2.destroy()
        self.poga3.destroy()

        if self.theme == 'wedding':
            button_start = PhotoImage(file = 'pictures/wedding-bg.png')
            self.fons = c.create_image(432,279, image = button_start)
            print('kaazs')
        elif self.theme == 'smt':
            pass

        print(gender)

    

Game()

mainloop()
