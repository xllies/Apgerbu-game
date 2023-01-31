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
        self.last_top = None
        self.last_top_rack = None
        self.last_bot = None
        self.last_bot_rack = None
        self.last_pair = None
        self.last_pair_rack = None
        self.last_socks = None
        self.last_socks_rack = None
        self.last_accesorie = None
        self.last_accesorie_rack = None
        self.top_on = None
        self.bot_on = None
        self.socks_on = None
        self.pair_on = None
        self.accesorie_on = None

        bg_start = PhotoImage(file = 'pictures/bg/home-bg.png')
        bg_choose = PhotoImage(file = 'pictures/bg/choose-lvl.png')
        bg_gender = PhotoImage(file = 'pictures/bg/gender-bg.png')
        bg_wedding = PhotoImage(file = 'pictures/bg/wedding-bg.png')
        bg_school = PhotoImage(file = 'pictures/bg/school-bg.png')
        bg_beach = PhotoImage(file = 'pictures/bg/beach-bg.png')
        bg_party = PhotoImage(file = 'pictures/bg/party-bg.png')
        bg_buizness = PhotoImage(file = 'pictures/bg/wedding-bg.png')
        bg_closet = PhotoImage(file = 'pictures/bg/fons.png')
        bg_result = PhotoImage(file= 'pictures/bg/score-bg.png' )

        button_start = PhotoImage(file = 'pictures/start-button.png')
        poga_woman = PhotoImage(file = 'pictures/poga-woman.png')
        poga_man = PhotoImage(file = 'pictures/poga-man.png')
        poga_rand = PhotoImage(file = 'pictures/poga-rand.png')
        destroy = PhotoImage(file = 'pictures/destroy.png')
        bulta = PhotoImage(file = 'pictures/bulta.png')
        gatavs_poga = PhotoImage(file = 'pictures/gatavs-poga.png')
        atkartot_poga = PhotoImage(file = 'pictures/atkartot-poga.png')

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
        on_man_bot6 = PhotoImage(file = 'pictures/man-clothes/bot6.png')

        on_man_socks1 = PhotoImage(file = 'pictures/man-clothes/socks1.png')
        on_man_socks2 = PhotoImage(file = 'pictures/man-clothes/socks2.png')

        on_man_accesorie1 = PhotoImage(file = 'pictures/man-clothes/accesorie1.png')
        on_man_accesorie2 = PhotoImage(file = 'pictures/man-clothes/accesorie2.png')
        on_man_accesorie3 = PhotoImage(file = 'pictures/man-clothes/accesorie3.png')

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

        man_socks1_light = PhotoImage(file = 'pictures/man-rack-clothes/socks1-light.png')
        man_socks2_light = PhotoImage(file = 'pictures/man-rack-clothes/socks2-light.png')  


        man_accesorie1 = PhotoImage(file = 'pictures/man-rack-clothes/accesorie1.png')
        man_accesorie2 = PhotoImage(file = 'pictures/man-rack-clothes/accesorie2.png')
        man_accesorie3 = PhotoImage(file = 'pictures/man-rack-clothes/accesorie3.png')

        on_man_accesorie1 = PhotoImage(file = 'pictures/man-clothes/accesorie1.png')
        on_man_accesorie2 = PhotoImage(file = 'pictures/man-clothes/accesorie2.png')
        on_man_accesorie3 = PhotoImage(file = 'pictures/man-clothes/accesorie3.png')

        man_accesorie1_light = PhotoImage(file = 'pictures/man-rack-clothes/accesorie1-light.png')
        man_accesorie2_light = PhotoImage(file = 'pictures/man-rack-clothes/accesorie2-light.png')
        man_accesorie3_light = PhotoImage(file = 'pictures/man-rack-clothes/accesorie3-light.png')
# ---------------------------------------------------------------# WOMAN ------------------------------------------
        woman = PhotoImage(file = 'pictures/woman.png') 

        on_woman_top1 = PhotoImage(file = 'pictures/woman-clothes/top1.png')
        on_woman_top2 = PhotoImage(file = 'pictures/woman-clothes/top2.png')
        on_woman_top3 = PhotoImage(file = 'pictures/woman-clothes/top3.png')
        on_woman_top4 = PhotoImage(file = 'pictures/woman-clothes/top4.png')
        on_woman_top5 = PhotoImage(file = 'pictures/woman-clothes/top5.png')
        on_woman_top6 = PhotoImage(file = 'pictures/woman-clothes/top6.png')

        on_woman_bot1 = PhotoImage(file = 'pictures/woman-clothes/bot1.png')
        on_woman_bot2 = PhotoImage(file = 'pictures/woman-clothes/bot2.png')
        on_woman_bot3 = PhotoImage(file = 'pictures/woman-clothes/bot3.png')
        on_woman_bot4 = PhotoImage(file = 'pictures/woman-clothes/bot4.png')
        on_woman_bot5 = PhotoImage(file = 'pictures/woman-clothes/bot5.png')
        on_woman_bot6 = PhotoImage(file = 'pictures/woman-clothes/bot6.png')

        on_woman_socks1 = PhotoImage(file = 'pictures/woman-clothes/socks1.png')
        on_woman_socks2 = PhotoImage(file = 'pictures/woman-clothes/socks2.png')

        on_woman_accesorie1 = PhotoImage(file = 'pictures/woman-clothes/accesorie1.png')
        on_woman_accesorie2 = PhotoImage(file = 'pictures/woman-clothes/accesorie2.png')
        on_woman_accesorie3 = PhotoImage(file = 'pictures/woman-clothes/accesorie3.png')

        on_woman_pair1 = PhotoImage(file = 'pictures/woman-clothes/pair1.png')
        on_woman_pair2 = PhotoImage(file = 'pictures/woman-clothes/pair2.png')
        on_woman_pair3 = PhotoImage(file = 'pictures/woman-clothes/pair3.png')
        on_woman_pair4 = PhotoImage(file = 'pictures/woman-clothes/pair4.png')

        woman_top1 = PhotoImage(file = 'pictures/woman-rack-clothes/top1.png')
        woman_top2 = PhotoImage(file = 'pictures/woman-rack-clothes/top2.png')
        woman_top3 = PhotoImage(file = 'pictures/woman-rack-clothes/top3.png')
        woman_top4 = PhotoImage(file = 'pictures/woman-rack-clothes/top4.png')
        woman_top5 = PhotoImage(file = 'pictures/woman-rack-clothes/top5.png')
        woman_top6 = PhotoImage(file = 'pictures/woman-rack-clothes/top6.png')
        woman_bot1 = PhotoImage(file = 'pictures/woman-rack-clothes/bot1.png')
        woman_bot2 = PhotoImage(file = 'pictures/woman-rack-clothes/bot2.png')
        woman_bot3 = PhotoImage(file = 'pictures/woman-rack-clothes/bot3.png')
        woman_bot4 = PhotoImage(file = 'pictures/woman-rack-clothes/bot4.png')
        woman_bot5 = PhotoImage(file = 'pictures/woman-rack-clothes/bot5.png')
        woman_bot6 = PhotoImage(file = 'pictures/woman-rack-clothes/bot6.png')

        woman_socks1 = PhotoImage(file = 'pictures/woman-rack-clothes/socks1.png')
        woman_socks2 = PhotoImage(file = 'pictures/woman-rack-clothes/socks2.png')

        woman_socks1_light = PhotoImage(file = 'pictures/woman-rack-clothes/socks1-light.png')
        woman_socks2_light = PhotoImage(file = 'pictures/woman-rack-clothes/socks2-light.png')  

        woman_pair1 = PhotoImage(file = 'pictures/woman-rack-clothes/pair1.png')
        woman_pair2 = PhotoImage(file = 'pictures/woman-rack-clothes/pair2.png')
        woman_pair3 = PhotoImage(file = 'pictures/woman-rack-clothes/pair3.png')
        woman_pair4 = PhotoImage(file = 'pictures/woman-rack-clothes/pair4.png')

        woman_accesorie1 = PhotoImage(file = 'pictures/woman-rack-clothes/accesorie1.png')
        woman_accesorie2 = PhotoImage(file = 'pictures/woman-rack-clothes/accesorie2.png')
        woman_accesorie3 = PhotoImage(file = 'pictures/woman-rack-clothes/accesorie3.png')

        woman_accesorie3_light = PhotoImage(file = 'pictures/woman-rack-clothes/accesorie3-light.png')


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
        self.bg_result = bg_result

        self.poga_woman = poga_woman
        self.poga_man = poga_man
        self.poga_rand = poga_rand
        self.destroy = destroy
        self.bulta = bulta
        self.gatavs_poga = gatavs_poga
        self.atkartot_poga = atkartot_poga

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
        self.on_man_bot6 = on_man_bot6

        self.on_man_socks1 = on_man_socks1
        self.on_man_socks2 = on_man_socks2

        self.on_man_pair1 = on_man_pair1
        self.on_man_pair2 = on_man_pair2
        self.on_man_pair3 = on_man_pair3
        self.on_man_pair4 = on_man_pair4

        self.on_man_accesorie1 = on_man_accesorie1
        self.on_man_accesorie2 = on_man_accesorie2
        self.on_man_accesorie3 = on_man_accesorie3

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
                            on_man_bot6,
                            on_man_pair1,
                            on_man_pair2,
                            on_man_pair3,
                            on_man_pair4,
                            on_man_socks1,
                            on_man_socks2,
                            on_man_accesorie1,
                            on_man_accesorie2,
                            on_man_accesorie3]
        self.man_rack_clothes = [man_top1,
                            man_top2,
                            man_top3,
                            man_top4,
                            man_top5,
                            man_top6,
                            man_bot1,
                            man_bot2,
                            man_bot3,
                            man_bot4,
                            man_bot5,
                            man_bot6,
                            man_socks1,
                            man_socks2,
                            man_socks1_light,
                            man_socks2_light,
                            man_pair1,
                            man_pair2,
                            man_pair3,
                            man_pair4,
                            man_accesorie1,
                            man_accesorie2,
                            man_accesorie3,
                            man_accesorie1_light,
                            man_accesorie2_light,
                            man_accesorie3_light]

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

        self.man_socks1_light = man_socks1_light
        self.man_socks2_light = man_socks2_light

        self.man_accesorie1 = man_accesorie1
        self.man_accesorie2 = man_accesorie2
        self.man_accesorie3 = man_accesorie3

        self.man_accesorie1_light = man_accesorie1_light
        self.man_accesorie2_light = man_accesorie2_light
        self.man_accesorie3_light = man_accesorie3_light

# ---------------------------------------------------------------# WOMAN ------------------------------------------
        self.woman = woman
       
        self.on_woman_top1 = on_woman_top1
        self.on_woman_top2 = on_woman_top2
        self.on_woman_top3 = on_woman_top3
        self.on_woman_top4 = on_woman_top4
        self.on_woman_top5 = on_woman_top5
        self.on_woman_top6 = on_woman_top6

        self.on_woman_bot1 = on_woman_bot1
        self.on_woman_bot2 = on_woman_bot2
        self.on_woman_bot3 = on_woman_bot3
        self.on_woman_bot4 = on_woman_bot4
        self.on_woman_bot5 = on_woman_bot5
        self.on_woman_bot6 = on_woman_bot6

        self.on_woman_socks1 = on_woman_socks1
        self.on_woman_socks2 = on_woman_socks2

        self.on_woman_pair1 = on_woman_pair1
        self.on_woman_pair2 = on_woman_pair2
        self.on_woman_pair3 = on_woman_pair3
        self.on_woman_pair4 = on_woman_pair4

        self.woman_clothes = [on_woman_top1,
                            on_woman_top2,
                            on_woman_top3,
                            on_woman_top4,
                            on_woman_top5,
                            on_woman_top6,
                            on_woman_bot1,
                            on_woman_bot2,
                            on_woman_bot3,
                            on_woman_bot4,
                            on_woman_bot5,
                            on_woman_bot6,
                            on_woman_pair1,
                            on_woman_pair2,
                            on_woman_pair3,
                            on_woman_pair4,
                            on_woman_socks1,
                            on_woman_socks2,
                            on_woman_accesorie1,
                            on_woman_accesorie2,
                            on_woman_accesorie3]
        self.woman_rack_clothes = [woman_top1,
                            woman_top2,
                            woman_top3,
                            woman_top4,
                            woman_top5,
                            woman_top6,
                            woman_bot1,
                            woman_bot2,
                            woman_bot3,
                            woman_bot4,
                            woman_bot5,
                            woman_bot6,
                            woman_socks1,
                            woman_socks2,
                            # woman_socks1_light,
                            # woman_socks2_light,
                            woman_pair1,
                            woman_pair2,
                            woman_pair3,
                            woman_pair4,
                            woman_accesorie1,
                            woman_accesorie2,
                            woman_accesorie3,
                            # woman_accesorie1_light,
                            # woman_accesorie2_light,
                            # woman_accesorie3_light
                            ]
        self.woman_top1 = woman_top1
        self.woman_top2 = woman_top2
        self.woman_top3 = woman_top3
        self.woman_top4 = woman_top4
        self.woman_top5 = woman_top5
        self.woman_top6 = woman_top6

        self.woman_bot1 = woman_bot1
        self.woman_bot2 = woman_bot2
        self.woman_bot3 = woman_bot3
        self.woman_bot4 = woman_bot4
        self.woman_bot5 = woman_bot5
        self.woman_bot6 = woman_bot6

        self.woman_pair1 = woman_pair1
        self.woman_pair2 = woman_pair2
        self.woman_pair3 = woman_pair3
        self.woman_pair4 = woman_pair4

        self.woman_socks1 = woman_socks1
        self.woman_socks2 = woman_socks2

        self.woman_socks1_light = woman_socks1_light
        self.woman_socks2_light = woman_socks2_light

        self.woman_accesorie1 = woman_accesorie1
        self.woman_accesorie2 = woman_accesorie2
        self.woman_accesorie3 = woman_accesorie3

        self.woman_accesorie3_light = woman_accesorie3_light


 
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
            self.fons = c.create_image(432,279, image = self.bg_wedding)
            

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
        

        self.accesorie1_light = c.create_image(808, 146, image = self.man_accesorie1_light)
        self.accesorie2_light = c.create_image(806, 195, image = self.man_accesorie2_light)
        c.move(self.accesorie1_light, -600, -600)
        c.move(self.accesorie2_light, -600, -600)


        self.accesorie1 = c.create_image(808, 146, image = self.woman_accesorie1,tags='drebe')
        self.accesorie2 = c.create_image(806, 195, image = self.woman_accesorie2,tags='drebe')

        

        bulta1 = c.create_image(804, 94, image = self.bulta)
        bulta2 = c.create_image(804, 307, image = self.bulta)
        self.stage1 = 'first'
        self.stage2 = 'first'

        if gender == 0:
            c.create_image(175, 291, image = self.woman)

            self.accesorie3 = c.create_image(810, 240, image = self.woman_accesorie3, tags='drebe')
            self.accesorie3_light = c.create_image(806, 195, image = self.man_accesorie3_light)
            c.move(self.accesorie3_light, -600, -600)

            self.top1 = c.create_image(432, 142, image = self.woman_top1, tags='drebe')
            self.top2 = c.create_image(560, 153, image = self.woman_top2, tags='drebe')
            self.top3 = c.create_image(692, 163, image = self.woman_top3, tags='drebe')
            self.top4 = c.create_image(429, 162, image = self.woman_top4, tags='drebe')
            self.top5 = c.create_image(560, 153, image = self.woman_top5, tags='drebe')
            self.top6 = c.create_image(692, 189, image = self.woman_top6, tags='drebe')

            c.move(self.top4, 1600, 1600)
            c.move(self.top5, 1600, 1600)
            c.move(self.top6, 1600, 1600)

            self.bot1 = c.create_image(441, 399, image = self.woman_bot1, tags='drebe')
            self.bot2 = c.create_image(573, 376, image = self.woman_bot2, tags='drebe')
            self.bot3 = c.create_image(706, 352, image = self.woman_bot3, tags='drebe')
            self.bot4 = c.create_image(444, 400, image = self.woman_bot4, tags='drebe')
            self.bot5 = c.create_image(574, 392, image = self.woman_bot5, tags='drebe')
            self.bot6 = c.create_image(703, 391, image = self.woman_bot6, tags='drebe')

            c.move(self.bot4, 1600, 1600)
            c.move(self.bot5, 1600, 1600)
            c.move(self.bot6, 1600, 1600)

            self.pair1 = c.create_image(463, 510, image = self.woman_pair1, tags='drebe')
            self.pair2 = c.create_image(542, 505, image = self.woman_pair2, tags='drebe')
            self.pair3 = c.create_image(625, 505, image = self.woman_pair3, tags='drebe')
            self.pair4 = c.create_image(721, 505, image = self.woman_pair4, tags='drebe')

            self.socks1 = c.create_image(815, 394, image = self.woman_socks1, tags='drebe')
            self.socks2 = c.create_image(813, 475, image = self.woman_socks2, tags='drebe')

            self.socks1_light = c.create_image(815, 394, image = self.woman_socks1_light)
            self.socks2_light = c.create_image(813, 475, image = self.woman_socks2_light)

            self.gender = 'woman'
            
        if gender == 1:
            c.create_image(190, 290, image = self.man)

            self.accesorie3 = c.create_image(810, 240, image = self.man_accesorie3, tags='drebe')
            self.accesorie3_light = c.create_image(806, 195, image = self.man_accesorie3_light)
            c.move(self.accesorie3_light, -600, -600)

            self.top1 = c.create_image(425, 150, image = self.man_top1, tags='top')
            self.top2 = c.create_image(560, 147, image = self.man_top2, tags='top')
            self.top3 = c.create_image(692, 157, image = self.man_top3, tags='top')

            self.top4 = c.create_image(427, 157, image = self.man_top4, tags='top')
            self.top5 = c.create_image(557, 161, image = self.man_top5, tags='top')
            self.top6 = c.create_image(692, 154, image = self.man_top6, tags='top')

            c.move(self.top4, 1600, 1600)
            c.move(self.top5, 1600, 1600)
            c.move(self.top6, 1600, 1600)



            self.bot1 = c.create_image(443, 400, image = self.man_bot1, tags='bot')
            self.bot2 = c.create_image(574, 375, image = self.man_bot2, tags='bot')
            self.bot3 = c.create_image(706, 362, image = self.man_bot3, tags='bot')

            self.bot4 = c.create_image(445, 383, image = self.man_bot4, tags='bot')
            self.bot5 = c.create_image(577, 392, image = self.man_bot5, tags='bot')
            self.bot6 = c.create_image(702, 398, image = self.man_bot6, tags='bot')

            c.move(self.bot4, 1600, 1600)
            c.move(self.bot5, 1600, 1600)
            c.move(self.bot6, 1600, 1600)

            self.pair1 = c.create_image(463, 510, image = self.man_pair1, tags='drebe')
            self.pair2 = c.create_image(542, 505, image = self.man_pair2, tags='drebe')
            self.pair3 = c.create_image(625, 505, image = self.man_pair3, tags='drebe')
            self.pair4 = c.create_image(721, 505, image = self.man_pair4, tags='drebe')

            self.socks1 = c.create_image(815, 394, image = self.man_socks1, tags='drebe')
            self.socks2 = c.create_image(813, 475, image = self.man_socks2, tags='drebe')

            self.socks1_light = c.create_image(815, 394, image = self.man_socks1_light)
            self.socks2_light = c.create_image(813, 475, image = self.man_socks2_light)

            self.gender = 'man'


        print(gender)

        self.gatavs_pogaa = Button(c,image=self.gatavs_poga, command=lambda:Game.result(self, self.last_top, self.last_bot, self.last_socks, self.last_pair, self.last_accesorie), background='#6B4531', activebackground='#6B4531', bd=0)
        self.gatavs_pogaa = Button(c,image=self.gatavs_poga, command=lambda:Game.choose_level(self),background='#6B4531', activebackground='#6B4531', bd=0)
        self.gatavs_pogaa.place(x=252,y=473)

        self.test = Button(c,image=self.gatavs_poga, command=lambda:Game.choose_level(self),background='#6B4531', activebackground='#6B4531', bd=0)
        self.test.place(x=8000,y=8000)
        # c.tag_bind('drebe', '<Button-1>', Game.tryy)

        c.tag_bind(bulta1, '<Button-1>', lambda xx :Game.bultaa(self, 1))
        c.tag_bind(bulta2, '<Button-1>', lambda x:Game.bultaa(self, 2))

        c.tag_bind(self.top1, '<Button-1>', lambda a :Game.tryy(self,0, self.top1, 1))
        c.tag_bind(self.top2, '<Button-1>', lambda a :Game.tryy(self,1, self.top2, 2))
        c.tag_bind(self.top3, '<Button-1>', lambda a :Game.tryy(self,2, self.top3, 3))

        c.tag_bind(self.top4, '<Button-1>', lambda a :Game.tryy(self,3, self.top4, 4))
        c.tag_bind(self.top5, '<Button-1>', lambda a :Game.tryy(self,4, self.top5, 5))
        c.tag_bind(self.top6, '<Button-1>', lambda a :Game.tryy(self,5, self.top6, 6))
 
        c.tag_bind(self.bot1, '<Button-1>', lambda a :Game.tryy(self,6, self.bot1, 1))
        c.tag_bind(self.bot2, '<Button-1>', lambda a :Game.tryy(self,7, self.bot2, 2))
        c.tag_bind(self.bot3, '<Button-1>', lambda a :Game.tryy(self,8, self.bot3, 3))
        c.tag_bind(self.bot4, '<Button-1>', lambda a :Game.tryy(self,9, self.bot4, 4))
        c.tag_bind(self.bot5, '<Button-1>', lambda a :Game.tryy(self,10, self.bot5, 5))
        c.tag_bind(self.bot6, '<Button-1>', lambda a :Game.tryy(self,11, self.bot6, 6))
        
        c.tag_bind(self.socks1, '<Button-1>', lambda a :Game.tryy(self,16, self.socks1,1, self.socks1_light))
        c.tag_bind(self.socks2, '<Button-1>', lambda a :Game.tryy(self,17, self.socks2,2, self.socks2_light))
        c.tag_bind(self.man_socks1, '<Button-1>', lambda a :Game.tryy(self,16, self.socks1, self.man_socks1_light))
        c.tag_bind(self.man_socks2, '<Button-1>', lambda a :Game.tryy(self,17, self.socks2, self.man_socks2_light))

        c.tag_bind(self.man_socks1_light, '<Button-1>', lambda a :Game.back(self,2,self.socks1, self.man_socks1_light, 815, 394,186, 497))
        c.tag_bind(self.man_socks2_light, '<Button-1>', lambda a :Game.back(self,2,self.socks2, self.man_socks2_light, 813, 475, 187, 503))

        c.tag_bind(self.pair1, '<Button-1>', lambda a :Game.tryy(self,12, self.pair1, 1))
        c.tag_bind(self.pair2, '<Button-1>', lambda a :Game.tryy(self,13, self.pair2, 2))
        c.tag_bind(self.pair3, '<Button-1>', lambda a :Game.tryy(self,14, self.pair3, 3))
        c.tag_bind(self.pair4, '<Button-1>', lambda a :Game.tryy(self,15, self.pair4, 4))


        c.tag_bind(self.accesorie1_light, '<Button-1>', lambda a :Game.back(self,1,self.accesorie1, self.accesorie1_light,808, 146, 184, 66))
        c.tag_bind(self.accesorie2_light, '<Button-1>', lambda a :Game.back(self,1,self.accesorie2, self.accesorie2_light, 806, 195, 188, 66))
        c.tag_bind(self.accesorie3_light, '<Button-1>', lambda a :Game.back(self,1,self.accesorie3, self.accesorie3_light, 810, 240, 188, 96))

        c.tag_bind(self.accesorie1, '<Button-1>', lambda a :Game.tryy(self,18, self.accesorie1, 1, self.accesorie1_light))
        c.tag_bind(self.accesorie2, '<Button-1>', lambda a :Game.tryy(self,19, self.accesorie2, 2, self.accesorie2_light))
        c.tag_bind(self.accesorie3, '<Button-1>', lambda a :Game.tryy(self,20, self.accesorie3, 3, self.accesorie3_light))


    def bultaa(self, pakaramais):
        if self.gender == 'man':
            if pakaramais == 1:
                if self.stage1 == 'first':
                    # c.delete('top')
                    c.move(self.top1, 1600, 1600)
                    c.move(self.top2, 1600, 1600)
                    c.move(self.top3, 1600, 1600)

                    c.move(self.top4, -1600, -1600)
                    c.move(self.top5, -1600, -1600)
                    c.move(self.top6, -1600, -1600)

                    self.stage1 = 'second'
                else:
                    # c.delete('top')
                    c.move(self.top1, -1600, -1600)
                    c.move(self.top2, -1600, -1600)
                    c.move(self.top3, -1600, -1600)

                    c.move(self.top4, 1600, 1600)
                    c.move(self.top5, 1600, 1600)
                    c.move(self.top6, 1600, 1600)

                    self.stage1 = 'first'
                
                
                

            if pakaramais == 2:
                if self.stage2 == 'first':
                    c.move(self.bot1, 1600, 1600)
                    c.move(self.bot2, 1600, 1600)
                    c.move(self.bot3, 1600, 1600)

                    c.move(self.bot4, -1600, -1600)
                    c.move(self.bot5, -1600, -1600)
                    c.move(self.bot6, -1600, -1600)       
                    self.stage2 = 'second'
                else:

                    c.move(self.bot1, -1600, -1600)
                    c.move(self.bot2, -1600, -1600)
                    c.move(self.bot3, -1600, -1600)

                    c.move(self.bot4, 1600, 1600)
                    c.move(self.bot5, 1600, 1600)
                    c.move(self.bot6, 1600, 1600)
                    self.stage2 = 'first'
        if self.gender == 'woman':
            if pakaramais == 1:
                if self.stage1 == 'first':
                    # c.delete('top')
                    c.move(self.top1, 1600, 1600)
                    c.move(self.top2, 1600, 1600)
                    c.move(self.top3, 1600, 1600)

                    c.move(self.top4, -1600, -1600)
                    c.move(self.top5, -1600, -1600)
                    c.move(self.top6, -1600, -1600)

                    self.stage1 = 'second'
                else:
                    # c.delete('top')
                    c.move(self.top1, -1600, -1600)
                    c.move(self.top2, -1600, -1600)
                    c.move(self.top3, -1600, -1600)

                    c.move(self.top4, 1600, 1600)
                    c.move(self.top5, 1600, 1600)
                    c.move(self.top6, 1600, 1600)

                    self.stage1 = 'first'
        
                
                

            if pakaramais == 2:
                if self.stage2 == 'first':
                    c.move(self.bot1, 1600, 1600)
                    c.move(self.bot2, 1600, 1600)
                    c.move(self.bot3, 1600, 1600)

                    c.move(self.bot4, -1600, -1600)
                    c.move(self.bot5, -1600, -1600)
                    c.move(self.bot6, -1600, -1600)       
                    self.stage2 = 'second'
                else:

                    c.move(self.bot1, -1600, -1600)
                    c.move(self.bot2, -1600, -1600)
                    c.move(self.bot3, -1600, -1600)

                    c.move(self.bot4, 1600, 1600)
                    c.move(self.bot5, 1600, 1600)
                    c.move(self.bot6, 1600, 1600)
                    self.stage2 = 'first'

        
    def back(self,witch, mover, light, x_start, y_start, x, y): 
        print('irr')
       
        if witch == 1: 
            c.delete(self.last_accesorie)
            self.last_accesorie = None
            self.last_accesorie_rack = None
        else:
            c.delete(self.last_socks)
            self.last_socks = None
            self.last_socks_rack = None

        c.move(mover, 800, 800)
        xx = (x - x_start)/200
        yy = (y - y_start)/200
        c.move(mover, (x - x_start), (y - y_start))
        for i in range (200):
            c.move(mover ,-xx,-yy)
            c.update()
        
        c.move(light, -600, -600)
        print('atnem',light)
        print(c.coords(light))


        

    def tryy(self, pic, name, number, light = None):
        # c.delete(name)
        self.daliitajs=100
        if self.gender=='man':
            if pic == 0:
                x=192
                y=206   
                x_start = 427
                y_start = 157                
            elif pic == 1:
                x=191
                y=206
                x_start, y_start = 557, 161

            elif pic == 2:
                x=192
                y=208
                x_start, y_start = 688, 137
            elif pic == 3:
                x=183
                y=213
                x_start, y_start = 425, 149
            elif pic == 4:
                x=180
                y=295
                x_start, y_start =560, 147
            elif pic == 5:
                x=190
                y=206
                x_start, y_start = 692, 157



            elif pic == 6:
                x=196
                y=392
                x_start, y_start = 443, 400
            elif pic == 7:
                x=186
                y=383
                x_start, y_start = 574, 375
            elif pic == 8:
                x=186
                y=333
                x_start, y_start = 706, 362
            elif pic == 9:
                x=191
                y=369
                x_start, y_start = 445, 383
            elif pic == 10:
                x=189
                y=378
                x_start, y_start = 577, 392
            elif pic == 11:
                x=187
                y=380
                x_start, y_start = 702, 398
            elif pic == 12:
                x=188
                y=524
                x_start, y_start =460, 510
            elif pic == 13:
                x=185
                y=520
                x_start, y_start =542, 505
            elif pic == 14:
                x=185
                y=517
                x_start, y_start =625, 505
            elif pic == 15:
                x=190
                y=518
                x_start, y_start =721, 505
            elif pic == 16:
                x=186
                y=497
                x_start, y_start =815, 394
            elif pic == 17:
                x=185
                y=503
                x_start, y_start =813, 475
            elif pic == 18:
                x=184 
                y=66
                x_start, y_start =808, 146
            elif pic == 19:
                x=188
                y=66
                x_start, y_start =806, 195
            elif pic == 20:
                x=187
                y=96
                x_start, y_start =810, 240
            else:
                return None


        if pic<=5:
            c.delete(self.last_top) #deletes last top outfit on
            top_on = c.create_image( x_start, y_start, image = self.man_clothes[pic], tags='tops')  #creates image on rack - after will be on human

            if self.last_top_rack != None:
                c.move(self.last_top_rack, 800, 800) 
            c.move(name, -800, -800)
            self.last_top = top_on
            self.last_top_rack = name  #array to create image after put back
            mover = top_on #the image that has been placed will be moved on human
            self.daliitajs = 100
            self.top_on = number

            
        elif pic<=11:
            c.delete(self.last_bot) #deletes last bot outfit on
            self.bot_on = c.create_image( x_start, y_start, image = self.man_clothes[pic], tags='bots')  #creates image on rack - after will be on human


            c.move(name, -800, -800)
            self.last_bot = self.bot_on
            self.last_bot_rack = name  #array to create image after put back

            mover = self.bot_on #the image that has been placed will be moved on human
            self.daliitajs = 100
            self.bot_on = number

        elif pic<=15:
            c.delete(self.last_pair)
            self.pair_on = c.create_image( x_start, y_start, image = self.man_clothes[pic], tags='shoe')
            if self.last_pair_rack != None:
                c.move(self.last_pair_rack, 800, 800)
            c.move(name, -800, -800)
            self.last_pair = self.pair_on
            self.last_pair_rack = name
            mover = self.pair_on
            self.daliitajs = 200
            self.pair_on = number

        elif pic<=17:
            c.delete(self.last_socks)
            socks_on = c.create_image( x_start, y_start, image = self.man_clothes[pic], tags='sock')
          
            if self.last_socks_rack != None:
                c.move(self.last_socks_rack, 800, 800) 

            c.move(name, -800, -800)
            self.last_socks = socks_on
            self.last_socks_rack = name  #array to create image after put back
      
            
            mover = socks_on #the image that has been placed will be moved on human

            self.daliitajs = 200

            self.socks_on = number


            if c.coords(light)[0] < 800:
                c.move(light, 600, 600)
                if c.coords(light)[0] < 800:
                    c.move(light, 600, 600)
                    print(c.coords(light))
                    print('pieskaita',light)    
            elif pic <=20:
                c.delete(self.last_accesorie)
                accesorie_on = c.create_image( x_start, y_start, image = self.man_clothes[pic], tags='acc')

                if self.last_accesorie_rack != None:
                    c.move(self.last_accesorie_rack, 800, 800) 


                c.move(name, -800, -800)
                print('pieskaita',light)
                print(c.coords(light)[0])
                if c.coords(light)[0] < 800:
                    c.move(light, 600, 600)
                    print(c.coords(light))
                    print('pieskaita',light)

                self.last_accesorie = accesorie_on
                self.last_accesorie_rack = name
                mover = accesorie_on

                self.daliitajs = 200

        if self.gender=='woman':
            if pic == 0:
                x=179
                y=190
                x_start = 422
                y_start = 132          
            elif pic == 1:
                x=176
                y=196
                x_start, y_start = 560, 153

            elif pic == 2:
                x=177
                y=207
                x_start, y_start = 692, 163
            elif pic == 3:
                x=178
                y=220
                x_start, y_start = 429, 162
            elif pic == 4:
                x=178
                y=182
                x_start, y_start =560, 153
            elif pic == 5:
                x=177
                y=266
                x_start, y_start = 692, 189



            elif pic == 6:
                x=180
                y=360
                x_start, y_start = 441, 399
            elif pic == 7:
                x=177
                y=306
                x_start, y_start = 573, 376
            elif pic == 8:
                x=176
                y=273
                x_start, y_start = 706, 352
            elif pic == 9:
                x=196
                y=357
                x_start, y_start = 444, 400
            elif pic == 10:
                x=178
                y=358
                x_start, y_start = 574, 392
            elif pic == 11:
                x=174
                y=360
                x_start, y_start = 703, 391
            
            elif pic == 12:
                x=172
                y=503
                x_start, y_start =463, 510
            elif pic == 13:
                x=173
                y=499
                x_start, y_start =542, 505
            elif pic == 14:
                x=185
                y=517
                x_start, y_start =625, 505
            elif pic == 15:
                x=175
                y=505
                x_start, y_start =721, 505
            elif pic == 16:
                x=186
                y=497
                x_start, y_start =815, 394
            elif pic == 17:
                x=185
                y=503
                x_start, y_start =813, 475
        
            elif pic == 18:
                x=184 
                y=66
                x_start, y_start =808, 146
            elif pic == 19:
                x=188
                y=66
                x_start, y_start =806, 195
            elif pic == 20:
                x=187
                y=96
                x_start, y_start =810, 240
            else:
                return None
                
            if pic<=5:
                    c.delete(self.last_top) #deletes last top outfit on
                    top_on = c.create_image( x_start, y_start, image = self.woman_clothes[pic], tags='tops')  #creates image on rack - after will be on human
                    print(self.last_top_rack)

                    if self.last_top_rack != None:
                        c.move(self.last_top_rack, 800, 800) 
                    c.move(name, -800, -800)
                    self.last_top = top_on
                    self.last_top_rack = name  #array to create image after put back
                    print(self.last_top_rack)
                    mover = top_on #the image that has been placed will be moved on human
                    self.daliitajs = 200

            elif pic<=11:
                    c.delete(self.last_bot) #deletes last bot outfit on
                    self.bot_on = c.create_image( x_start, y_start, image = self.woman_clothes[pic], tags='bots')  #creates image on rack - after will be on human
                    print(self.last_bot_rack)

                    if self.last_bot_rack != None:
                        c.move(self.last_bot_rack, 800, 800) 

                    c.move(name, -800, -800)
                    self.last_bot = self.bot_on
                    self.last_bot_rack = name  #array to create image after put back
                    print(self.last_bot_rack)
                    mover = self.bot_on #the image that has been placed will be moved on human
                    self.daliitajs = 200
            elif pic<=15:
                    c.delete(self.last_pair)
                    self.pair_on = c.create_image( x_start, y_start, image = self.woman_clothes[pic], tags='shoe')
                    if self.last_pair_rack != None:
                        c.move(self.last_pair_rack, 800, 800)
                    c.move(name, -800, -800)
                    self.last_pair = self.pair_on
                    self.last_pair_rack = name
                    print(self.last_pair_rack)
                    mover = self.pair_on
                    self.daliitajs = 200
            elif pic<=17:
                c.delete(self.last_sock)
                sock_on = c.create_image( x_start, y_start, image = self.woman_clothes[pic], tags='sock')

                if self.last_sock_rack != None:
                    c.move(self.last_sock_rack, 800, 800) 

                c.move(name, -800, -800)
                self.last_sock = sock_on
                self.last_sock_rack = name  #array to create image after put back
                print(self.last_sock_rack)

                mover = sock_on #the image that has been placed will be moved on human
                self.daliitajs = 200

                self.accesorie_on = number

                c.move(name, -800, -800)
  
                if c.coords(light)[0] < 800:
                    c.move(light, 600, 600)
  
            elif pic <=20:
                c.delete(self.last_accesorie)
                accesorie_on = c.create_image( x_start, y_start, image = self.woman_clothes[pic], tags='acc')

                if self.last_accesorie_rack != None:
                    c.move(self.last_accesorie_rack, 800, 800) 

                c.move(name, -800, -800)

                self.last_accesorie = accesorie_on
                self.last_accesorie_rack = name
                mover = accesorie_on    
                self.daliitajs = 200

        xx = (x-x_start)/self.daliitajs
        yy = (y-y_start)/self.daliitajs
        for i in range (self.daliitajs):
            
            x_start+=xx
            y_start+=yy
            c.move(mover,xx,yy)
            c.update()
        c.tag_raise("shoe")
        c.tag_raise("bots")
        c.tag_raise("tops")
        c.update()


            
            # c.moveto(on_top, x, y)
            
    def result(self, top, bot, socks, pair, accesories):
        c.delete('all')
        self.gatavs_pogaa.destroy()

        self.fons = c.create_image(432,279, image = self.bg_result)

        self.atbilde = []
        if self.gender == 'man':
            self.result = 0
            if top == None:
                self.atbilde.append('Tev tav nav uzvilkts krekls, bikses vai kurpes.')
                self.atbilde.append('Tāds apģērbs ētiski pareizs!')
                
            elif self.bot_on == None:
                self.atbilde.append('Tev tav nav uzvilkts krekls, bikses vai kurpes.')
                self.atbilde.append('Tāds apģērbs ētiski pareizs!')
            elif pair == None:
                self.atbilde.append('Tev tav nav uzvilkts krekls, bikses vai kurpes.')
                self.atbilde.append('Tāds apģērbs ētiski pareizs!')
            else:
                print(self.theme)
                if self.theme == 'wedding':

                    if self.bot_on == 2 or self.bot_on == 3:
                        print('self.bot_on2')
                        self.atbilde.append('Šorti vai saplēstas bikses nav piemērots svētku apģērbs!')
                        self.result += 2
                    elif self.bot_on == 4:
                        self.atbilde.append('Šīs bikses ir par īsu!')
                        self.result += 4
                    elif self.bot_on == 1:
                        self.atbilde.append('Džinsas nav īsti piemērots apģērbs kāzām!')
                        self.result += 6
                    elif self.bot_on == 5 or self.bot_on == 6:
                        self.result += 30


                    if self.top_on == 1 or self.top_on == 2:
                        self.atbilde.append('Maika vai džemperis nav piemērots apģērbs kāzām!')
                        self.result += 2
                    elif self.top_on == 4 or self.top_on == 5:
                        self.result += 30
                    elif self.top_on == 3 or self.top_on == 6:
                        self.atbilde.append('Uz kāzām augšā jāuzvelk kautkas svinēgāks!')
                        self.result += 6

                    if self.pair_on == 1 or self.pair_on == 2:
                        self.atbilde.append('Uz kāzām krosenes vai čības nav piemērotas!')
                        self.result += 4
                    elif self.pair_on == 3 or self.pair_on == 4:
                        self.result += 30

                    if self.socks_on == 2:
                        self.atbilde.append('Zeķes ir par spilgtu!')
                        self.result+=1

                    elif self.socks_on ==1:
                        self.result+=5

                    if self.accesorie_on == 1:
                        self.atbilde.append('Šī cepure nav piemērota kāzām!')
                        print('jii')
                        print(self.atbilde)
                        self.result-=2
                    else:
                        self.result+=2



            if self.theme == 'school':

                    if self.bot_on == 2 or self.bot_on == 3:
    
                        self.atbilde.append('Šorti vai saplēstas bikses nav piemērots apģērbs skolai!')
                        self.result += 2
                    elif self.bot_on == 4 and self.socks_on == None:
                        self.atbilde.append('Šīs bikses ir par īsu, ar tām jāvelk zeķes!')
                        self.result += 6
                    elif self.bot_on == 5 or self.bot_on == 6:
                        self.atbilde.append('Šīs bikses ir pārāk svinīgs apģērbs skolai!')
                        self.result += 6
                    elif self.bot_on == 1 or self.bot_on == 4:
                        self.result += 30


                    if self.top_on == 3 or self.top_on == 2 or self.top_on == 6:
                        self.result += 30
                    elif self.top_on == 1:
                        self.result += 5
                        self.atbilde.append('Uz skolu maika nav piemērots apģērbs!')
                    elif self.top_on == 4 or self.top_on == 5:
                        self.atbilde.append('Augšā jāvelk kautkas ne tik svinīgs!')
                        self.result += 6


                    if self.pair_on == 2:
                        self.result += 30
                    elif self.pair_on == 3 or self.pair_on == 4:
                        self.atbilde.append('Šīs kurpes ir par svinīgu skolai!')
                        self.result += 5
                    else:
                        self.atbilde.append('Čības nav piemērots apģērbs skolai skolai!')
                        self.result += 3


                    if self.socks_on != None:
                        self.result+=5
                    else:
                        self.atbilde.append('Ir jāuzvelk zeķes!')

                    if self.accesorie_on == None:
                        self.result+=5
                    else:
                        self.atbilde.append('Skolā nav jāvelk cepure vai saulesbrilles!')



            
            if self.theme == 'beach':

                    if self.bot_on == 1 or self.bot_on == 2:
    
                        self.atbilde.append('Džinsas piemērotas īsti pludmalei!')
                        self.result += 19

                    elif self.bot_on == 5 or self.bot_on == 5:
    
                        self.atbilde.append('Uzvilktās bikses ir par svinīgu!')
                        self.result += 9

                    elif self.bot_on == 3 or self.bot_on == 4:
                        self.result += 30



                    if self.top_on == 1 or self.top_on == 2:
                        self.result += 30

                    elif self.top_on == 4 or self.top_on == 5:
                        self.result += 10
                        self.atbilde.append('Augšā nav jāvelk kautkas tik svinīgs!')

                    elif self.top_on == 2 or self.top_on == 6:
                        self.atbilde.append('Džemperī pludmalē būtu par karstu!')
                        self.result += 15


                    if self.pair_on == 1:
                        self.result += 30
                    elif self.pair_on == 3 or self.pair_on == 4:
                        self.atbilde.append('Šīs kurpes ir par svinīgu pludmalei!')
                        self.result += 5
                    else:
                        self.atbilde.append('Labāk uz pludmali vilkt čības!')
                        self.result += 25


                    if self.accesorie_on == None:
                        pass
                    else:
                        self.result+=5
                        self.atbilde.append('Uz pludmali jāuzvelk cepure vai saulesbrilles!')

        print('RESULTS')
        print(self.atbilde)


        self.atkartott = Button(c,image=self.atkartot_poga, command=lambda:Game.play_again(self),background='#7FAD71', activebackground='#7FAD71', bd=0)
        self.atkartott.place(x=351,y=473)
   
        x = 200
        y = 250
        if self.atbilde != []:
            for i in self.atbilde:
                c.create_text(x, y, text = i)
                y += 50
        else:
            c.create_text(x, y, text = 'Tu esi piemēroti saģērbis doto cilvēku!')

        print(self.result)
        c.create_text(630, 210, text = str(self.result)+'%', font=("Arial", 40))


                    

                    
    def play_again(self):
        c.delete('all')
        self.atkartott.destroy()
        Game()



            



Game()

mainloop()