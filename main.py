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
        

        bg_start = PhotoImage(file = 'pictures/bg/home-bg.png')
        bg_choose = PhotoImage(file = 'pictures/bg/choose-lvl.png')
        bg_gender = PhotoImage(file = 'pictures/bg/gender-bg.png')
        bg_wedding = PhotoImage(file = 'pictures/bg/wedding-bg.png')
        bg_school = PhotoImage(file = 'pictures/bg/school-bg.png')
        bg_beach = PhotoImage(file = 'pictures/bg/beach-bg.png')
        bg_party = PhotoImage(file = 'pictures/bg/party-bg.png')
        bg_buizness = PhotoImage(file = 'pictures/bg/wedding-bg.png')
        bg_closet = PhotoImage(file = 'pictures/bg/fons.png')

        button_start = PhotoImage(file = 'pictures/start-button.png')
        poga_woman = PhotoImage(file = 'pictures/poga-woman.png')
        poga_man = PhotoImage(file = 'pictures/poga-man.png')
        poga_rand = PhotoImage(file = 'pictures/poga-rand.png')
        destroy = PhotoImage(file = 'pictures/destroy.png')
        bulta = PhotoImage(file = 'pictures/bulta.png')

        baloon1 = PhotoImage(file = 'pictures/baloon-wedding.png')
        baloon2 = PhotoImage(file = 'pictures/baloon-school.png')
        baloon3 = PhotoImage(file = 'pictures/baloon-beach.png')
        baloon4 = PhotoImage(file = 'pictures/baloon-party.png')
        baloon5 = PhotoImage(file = 'pictures/baloon-buizness.png')

        hanger1 = PhotoImage(file = 'pictures/hanger1.png')
        hanger2 = PhotoImage(file = 'pictures/hanger2.png')
        coathanger = PhotoImage(file = 'pictures/coathanger.png')
        pantshanger = PhotoImage(file = 'pictures/pantshanger.png')

# ---------------------------------------------------------------# MAN ------------------------------------------

        man = PhotoImage(file = 'pictures/man.png')
        

        on_man_top1 = PhotoImage(file = 'pictures/man-clothes/top1.png')
        on_man_top2 = PhotoImage(file = 'pictures/man-clothes/top2.png')
        on_man_top3 = PhotoImage(file = 'pictures/man-clothes/top3.png')
        on_man_top4 = PhotoImage(file = 'pictures/man-clothes/top4.png')
        on_man_top5 = PhotoImage(file = 'pictures/man-clothes/top5.png')
        on_man_top6 = PhotoImage(file = 'pictures/man-clothes/top6.png')

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


        man_top1 = PhotoImage(file = 'pictures/man-rack-clothes/top1.png')
        man_top2 = PhotoImage(file = 'pictures/man-rack-clothes/top2.png')
        man_top3 = PhotoImage(file = 'pictures/man-rack-clothes/top3.png')
        man_top4 = PhotoImage(file = 'pictures/man-rack-clothes/top4.png')
        man_top5 = PhotoImage(file = 'pictures/man-rack-clothes/top5.png')
        man_top6 = PhotoImage(file = 'pictures/man-rack-clothes/top6.png')

        man_bot1 = PhotoImage(file = 'pictures/man-rack-clothes/bot1.png')
        man_bot2 = PhotoImage(file = 'pictures/man-rack-clothes/bot2.png')
        man_bot3 = PhotoImage(file = 'pictures/man-rack-clothes/bot3.png')
        man_bot4 = PhotoImage(file = 'pictures/man-rack-clothes/bot4.png')
        man_bot5 = PhotoImage(file = 'pictures/man-rack-clothes/bot5.png')
        man_bot6 = PhotoImage(file = 'pictures/man-rack-clothes/bot6.png')

        man_pair1 = PhotoImage(file = 'pictures/man-rack-clothes/pair1.png')
        man_pair2 = PhotoImage(file = 'pictures/man-rack-clothes/pair2.png')
        man_pair3 = PhotoImage(file = 'pictures/man-rack-clothes/pair3.png')
        man_pair4 = PhotoImage(file = 'pictures/man-rack-clothes/pair4.png')

        man_socks1 = PhotoImage(file = 'pictures/man-rack-clothes/socks1.png')
        man_socks2 = PhotoImage(file = 'pictures/man-rack-clothes/socks2.png')


        man_accesorie1 = PhotoImage(file = 'pictures/man-rack-clothes/accesorie1.png')
        man_accesorie2 = PhotoImage(file = 'pictures/man-rack-clothes/accesorie2.png')
        man_accesorie3 = PhotoImage(file = 'pictures/man-rack-clothes/accesorie3.png')
# ---------------------------------------------------------------# WOMAN ------------------------------------------
        woman = PhotoImage(file = 'pictures/woman.png') 

        woman_top1 = PhotoImage(file = 'pictures/woman-rack-clothes/top1.png')
        woman_top2 = PhotoImage(file = 'pictures/woman-rack-clothes/top2.png')
        woman_top3 = PhotoImage(file = 'pictures/woman-rack-clothes/top3.png')
        woman_top4 = PhotoImage(file = 'pictures/woman-rack-clothes/top4.png')
        woman_top5 = PhotoImage(file = 'pictures/woman-rack-clothes/top5.png')
        woman_top6 = PhotoImage(file = 'pictures/woman-rack-clothes/top6.png')
        # woman_bot1 = PhotoImage(file = 'pictures/woman-rack-clothes/bot1.png')
        # woman_bot2 = PhotoImage(file = 'pictures/woman-rack-clothes/bot2.png')
        # woman_bot3 = PhotoImage(file = 'pictures/woman-rack-clothes/bot3.png')
        # woman_bot4 = PhotoImage(file = 'pictures/woman-rack-clothes/bot4.png')
        # woman_bot5 = PhotoImage(file = 'pictures/woman-rack-clothes/bot5.png')
        # woman_bot6 = PhotoImage(file = 'pictures/woman-rack-clothes/bot6.png')

        woman_accesorie1 = PhotoImage(file = 'pictures/woman-rack-clothes/accesorie1.png')
        woman_accesorie2 = PhotoImage(file = 'pictures/woman-rack-clothes/accesorie2.png')
        woman_accesorie3 = PhotoImage(file = 'pictures/woman-rack-clothes/accesorie3.png')


        self.bg_start = bg_start
        self.button_start = button_start
        self.bg_choose = bg_choose
        self.bg_gender = bg_gender
        self.bg_wedding = bg_wedding
        self.bg_school = bg_school
        self.bg_beach = bg_beach
        self.bg_party = bg_party
        self.bg_buizness = bg_buizness
        self.bg_closet = bg_closet

        self.poga_woman = poga_woman
        self.poga_man = poga_man
        self.poga_rand = poga_rand
        self.destroy = destroy
        self.bulta = bulta

        self.baloon1 = baloon1
        self.baloon2 = baloon2
        self.baloon3 = baloon3
        self.baloon4 = baloon4
        self.baloon5 = baloon5

        self.hanger1 = hanger1
        self.hanger2 = hanger2
        self.coathanger = coathanger
        self.pantshanger = pantshanger


# ---------------------------------------------------------------# WOMAN ------------------------------------------


        self.man = man
       
        self.on_man_top1 = on_man_top1
        self.on_man_top2 = on_man_top2
        self.on_man_top3 = on_man_top3
        self.on_man_top4 = on_man_top4
        self.on_man_top5 = on_man_top5
        self.on_man_top6 = on_man_top6

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

        self.man_clothes = [on_man_top1,
                            on_man_top2,
                            on_man_top3,
                            on_man_top4,
                            on_man_top5,
                            on_man_top6,
                            on_man_bot1,
                            on_man_bot2,
                            on_man_bot3,
                            on_man_bot4,
                            on_man_bot5,
                            on_man_socks1,
                            on_man_socks2,
                            on_man_pair1,
                            on_man_pair2,
                            on_man_pair3,
                            on_man_pair4]

        self.man_top1 = man_top1
        self.man_top2 = man_top2
        self.man_top3 = man_top3
        self.man_top4 = man_top4
        self.man_top5 = man_top5
        self.man_top6 = man_top6

        self.man_bot1 = man_bot1
        self.man_bot2 = man_bot2
        self.man_bot3 = man_bot3
        self.man_bot4 = man_bot4
        self.man_bot5 = man_bot5
        self.man_bot6 = man_bot6

        self.man_pair1 = man_pair1
        self.man_pair2 = man_pair2
        self.man_pair3 = man_pair3
        self.man_pair4 = man_pair4

        self.man_socks1 = man_socks1
        self.man_socks2 = man_socks2

        self.man_accesorie1 = man_accesorie1
        self.man_accesorie2 = man_accesorie2
        self.man_accesorie3 = man_accesorie3

# ---------------------------------------------------------------# WOMAN ------------------------------------------
        self.woman = woman

        self.woman_top1 = woman_top1
        self.woman_top2 = woman_top2
        self.woman_top3 = woman_top3
        self.woman_top4 = woman_top4
        self.woman_top5 = woman_top5
        self.woman_top6 = woman_top6

        # self.woman_bot1 = woman_bot1
        # self.woman_bot2 = woman_bot2
        # self.woman_bot3 = woman_bot3
        # self.woman_bot4 = woman_bot4
        # self.woman_bot5 = woman_bot5
        # self.woman_bot6 = woman_bot6

        self.woman_accesorie1 = woman_accesorie1
        self.woman_accesorie2 = woman_accesorie2
        self.woman_accesorie3 = woman_accesorie3


 
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
        self.baloon_btn5 = Button(c,image=self.baloon5, command=lambda:Game.gender(self, 'buizness'),background='#79C9F9', activebackground='#79C9F9', bd=0)
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

        self.poga4 = Button(c,image=self.destroy, command=lambda:Game.level_start(self, random.randint(0,1)),background='#7FAD71', activebackground='#7FAD71', bd=0)
        self.poga4.place(x=900,y=475)


    def level_start(self, gender):
        self.poga3.destroy()
        self.poga2.destroy()
        self.poga1.destroy()

        if self.theme == 'wedding':
            print(self.bg_wedding)
            self.fons = c.create_image(432,279, image = self.bg_wedding)
            print('kaazs')

        elif self.theme == 'school':
            self.fons = c.create_image(432,279, image = self.bg_school)

        elif self.theme == 'beach':
            self.fons = c.create_image(432,279, image = self.bg_beach)

        elif self.theme == 'party':
            self.fons = c.create_image(432,279, image = self.bg_party)

        elif self.theme == 'buizness':
            self.fons = c.create_image(432,279, image = self.bg_buizness)

        c.create_image(585,314, image = self.bg_closet)

        hanger1 = c.create_image(557,87, image = self.hanger1)
        c.create_image(429,98, image = self.coathanger)
        c.create_image(560,98, image = self.coathanger)
        c.create_image(692,98, image = self.coathanger)

        hanger2 = c.create_image(570,293, image = self.hanger2)
        c.create_image(443,298, image = self.pantshanger)
        c.create_image(574,298, image = self.pantshanger)
        c.create_image(705,298, image = self.pantshanger)
        
        woman_accesorie1 = c.create_image(808, 146, image = self.woman_accesorie1,tags='drebe')
        woman_accesorie2 = c.create_image(806, 195, image = self.woman_accesorie2,tags='drebe')

        bulta1 = c.create_image(804, 94, image = self.bulta)
        bulta2 = c.create_image(804, 307, image = self.bulta)
        self.stage1 = 'first'

        if gender == 0:
            c.create_image(175, 291, image = self.woman)

            accesorie3 = c.create_image(810, 240, image = self.woman_accesorie3, tags='drebe')

            top1 = c.create_image(440, 137, image = self.woman_top1, tags='drebe')
            top2 = c.create_image(560, 153, image = self.woman_top2, tags='drebe')
            top3 = c.create_image(692, 159, image = self.woman_top3, tags='drebe')

           

            # bot1 = c.create_image(440, 137, image = self.woman_bot1, tags='drebe')
            # bot2 = c.create_image(560, 153, image = self.woman_bot2, tags='drebe')
            # bot3 = c.create_image(692, 159, image = self.woman_bot3, tags='drebe')
            
            
        if gender == 1:
            c.create_image(175, 291, image = self.man)

            accesorie3 = c.create_image(810, 240, image = self.man_accesorie3, tags='drebe')

            top1 = c.create_image(425, 137, image = self.man_top1, tags='top')
            top2 = c.create_image(560, 147, image = self.man_top2, tags='top')
            top3 = c.create_image(692, 157, image = self.man_top3, tags='top')

            bot1 = c.create_image(443, 400, image = self.man_bot1, tags='bot')
            bot2 = c.create_image(574, 375, image = self.man_bot2, tags='bot')
            bot3 = c.create_image(706, 362, image = self.man_bot3, tags='bot')

            pair1 = c.create_image(460, 510, image = self.man_pair1, tags='drebe')
            pair2 = c.create_image(542, 505, image = self.man_pair2, tags='drebe')
            pair3 = c.create_image(625, 505, image = self.man_pair3, tags='drebe')
            pair4 = c.create_image(721, 505, image = self.man_pair4, tags='drebe')

            socks1 = c.create_image(815, 394, image = self.man_socks1, tags='drebe')
            socks2 = c.create_image(813, 475, image = self.man_socks2, tags='drebe')

            self.gender = 'man'

        print(gender)

        # c.tag_bind('drebe', '<Button-1>', Game.tryy)

        c.tag_bind(bulta1, '<Button-1>', lambda xx :Game.bultaa(self, 1))
        c.tag_bind(bulta2, '<Button-1>', lambda x:Game.bultaa(self, 2))

        top_clothes=[1,2,3]
        c.tag_bind(top1, '<Button-1>', lambda a :Game.tryy(self,'top', '1'))
        c.tag_bind(top2, '<Button-1>', lambda a :Game.tryy(self,'top', '2'))
        c.tag_bind(top3, '<Button-1>', lambda a :Game.tryy(self,'top', '3'))

    def bultaa(self, pakaramais):
        if self.gender == 'man':
            if pakaramais == 1:
                if self.stage1 == 'first':
                    c.delete('top')
                    top4 = c.create_image(427, 157, image = self.man_top4, tags='top')
                    top5 = c.create_image(557, 161, image = self.man_top5, tags='top')
                    self.stage1 = 'second'
                else:
                    c.delete('top')
                    top1 = c.create_image(425, 137, image = self.man_top1, tags='top')
                    top2 = c.create_image(560, 147, image = self.man_top2, tags='top')
                    top3 = c.create_image(692, 157, image = self.man_top3, tags='top')
                    self.stage1 = 'first'
            if pakaramais == 2:
                if self.stage1 == 'first':
                    c.delete('bot')
                    bot4 = c.create_image(445, 383, image = self.man_bot4, tags='bot')
                    bot5 = c.create_image(577, 392, image = self.man_bot5, tags='bot')
                    bot6 = c.create_image(702, 398, image = self.man_bot6, tags='bot')
                    self.stage1 = 'second'
                else:
                    c.delete('bot')
                    bot1 = c.create_image(443, 400, image = self.man_bot1, tags='bot')
                    bot2 = c.create_image(574, 375, image = self.man_bot2, tags='bot')
                    bot3 = c.create_image(706, 362, image = self.man_bot3, tags='bot')
                    self.stage1 = 'first'





    def tryy(self, place, count):

        if self.gender=='man':
            print('works')
            bilde = 'on_man_'+place+count
            on_top1 = c.create_image(100, 100, image = bilde, tags='on_top')

    

Game()

mainloop()
