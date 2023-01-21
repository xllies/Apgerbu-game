from tkinter import *

GARUMS = 558
PLATUMS = 864
logs = Tk()
logs.title('Ko vilkt?')

c = Canvas(logs, width=PLATUMS, height=GARUMS, bg='#4b6fa6') 
c.pack()

start_btn = PhotoImage(file = 'pictures/start-button.png')
home_fons = PhotoImage(file = 'pictures/home-bg.png')
chose_fons = PhotoImage(file = 'pictures/choose-lvl.png')

baloon1 = PhotoImage(file = 'pictures/baloon-wedding.png')
baloon2 = PhotoImage(file = 'pictures/baloon-school.png')
baloon3 = PhotoImage(file = 'pictures/baloon-beach.png')
baloon4 = PhotoImage(file = 'pictures/baloon-party.png')
baloon5 = PhotoImage(file = 'pictures/baloon-buizness.png')

class Game:
    def __init__(self, bg_start, button_start, bg_choose, baloon1, baloon2, baloon3, baloon4, baloon5):
        self.bg_start = bg_start
        self.button_start = button_start
        self.bg_choose = bg_choose

        self.baloon1 = baloon1
        self.baloon2 = baloon2
        self.baloon3 = baloon3
        self.baloon4 = baloon4
        self.baloon5 = baloon5

        Game.open_all(self)

    def open_all(self):
        
        self.fons = c.create_image(432,279, image = self.bg_start)
        self.start_poga = Button(c,image=self.button_start, command=lambda:Game.choose_level(self),background='#6B4531', activebackground='#6B4531', bd=0)
        self.start_poga.place(x=244,y=180)

    def choose_level(self):
        c.delete('all')
        self.start_poga.destroy()

        self.baloon_btn1 = Button(c,image=self.baloon1, command=lambda:Game.gender(self),background='#79C9F9', activebackground='#79C9F9', bd=0)
        self.baloon_btn1.place(x=43,y=83)
        self.baloon_btn2 = Button(c,image=self.baloon2, command=lambda:Game.gender(self),background='#79C9F9', activebackground='#79C9F9', bd=0)
        self.baloon_btn2.place(x=188,y=5)
        self.baloon_btn3 = Button(c,image=self.baloon3, command=lambda:Game.gender(self),background='#79C9F9', activebackground='#79C9F9', bd=0)
        self.baloon_btn3.place(x=362,y=116)
        self.baloon_btn4 = Button(c,image=self.baloon4, command=lambda:Game.gender(self),background='#79C9F9', activebackground='#79C9F9', bd=0)
        self.baloon_btn4.place(x=533,y=14)
        self.baloon_btn5 = Button(c,image=self.baloon5, command=lambda:Game.gender(self),background='#79C9F9', activebackground='#79C9F9', bd=0)
        self.baloon_btn5.place(x=688,y=116)


        self.fons = c.create_image(432,279, image = self.bg_choose)



    def gender(self):
        c.delete('all')
        self.baloon_btn1.destroy()
        self.baloon_btn2.destroy()
        self.baloon_btn3.destroy()
        self.baloon_btn4.destroy()
        self.baloon_btn5.destroy()

        woman = Button(c, text="woman", command=lambda: Game.level_start(self, 'woman'))
        woman.place(x=100,y=100)

        man = Button(c, text="man", command=lambda: Game.level_start(self, 'man'))
        man.place(x=300,y=100)



    def level_start():
        pass

    

Game(home_fons, start_btn, chose_fons, baloon1, baloon2, baloon3, baloon4, baloon5)

mainloop()
