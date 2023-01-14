from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt

from tkinter import ttk
from PIL import Image,ImageTk


GARUMS = 500
PLATUMS = 800
logs = Tk()
logs.title('Burbuļu spridzinātājs')

a = Canvas(logs, width=PLATUMS, height=GARUMS, bg='#4b6fa6') # mainīta bg krāsa
a.pack()

# kuģa_id = a.create_oval(0, 0, 40, 40, fill='#decbab')
# kuģa_id2 = a.create_oval(10, 20, 30, 30, fill='#ffffff')
# kuģa_id3 = a.create_oval(10, 10, 15, 15, fill='#24B7B9')
# kuģa_id4 = a.create_oval(25, 10, 30, 15, fill='#24B7B9')

def start_game(level, BURBUĻI_NEJAUŠI, ENEMY_NEJAUŠI, LAIKA_IEROBEŽOJUMS, MIN_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_ĀTRUMS, MIN_BURBUĻA_ĀTRUMS, MIN_ENEMY_RĀDIUSS, MAX_ENEMY_RĀDIUSS, MIN_ENEMY_ĀTRUMS, MAX_ENEMY_ĀTRUMS, fona_bilde, NEEDED_SCORE): #funkcija kura sāk spēli

    # fona_bilde = PhotoImage(file = 'pirmkods/a.png')  
    fons = a.create_image(402,252, image = fona_bilde)  #importo fonu un izveido bildi

    global spongijs
    img = PhotoImage(file = 'pirmkods/spongy311.png')
    spongijs = a.create_image(50,50, image = img, tags = 'ship')  #importo spengebob un izveido bildi

    global burger_img
    burger_img = (Image.open("pirmkods/burger.png"))#atver burgera bildi

    global enemy_img
    enemy_img = (Image.open("pirmkods/jellyy.png"))#atver medūzas bildi

    global lives_img
    lives_img = PhotoImage(file = 'pirmkods/h.png')



    KUĢA_RĀDIUSS = 15
    VID_X = PLATUMS / 2
    VID_Y = GARUMS / 2
    global x
    global y
    x, y = VID_X, VID_Y #izveido vērtības kas padarītas globālas

    # a.move(kuģa_id, VID_X, VID_Y)
    # a.move(kuģa_id2, VID_X, VID_Y)
    # a.move(kuģa_id3, VID_X, VID_Y)
    # a.move(kuģa_id4, VID_X, VID_Y)

    a.move(spongijs, x, y)

    global velx
    global vely
    velx = 0 #izveido vērtības
    vely = 0 #izveido vērtības




    def move():
        global x
        global y
        global velx
        global vely

        if x < 30 and pressed_x == 'a': #pārbauda vai pēdējā spiestā poga ir a un vai tā ir pie robežām
            velx = 0 #ja tā ir tad tiek noņemta velx vērtība, kas bija pieskaitīta piespiešot pogu a

        if x > PLATUMS-30 and pressed_x == 'd':  #pārbauda vai pēdējā spiestā poga ir d un vai tā ir pie robežām
            velx = 0

        if y < 30 and pressed_y == 'w':  #pārbauda vai pēdējā spiestā poga ir w un vai tā ir pie robežām
            vely = 0

        if y > GARUMS-30 and pressed_y == 's':  #pārbauda vai pēdējā spiestā poga ir s un vai tā ir pie robežām
            vely = 0

        x += velx #pieskaita koordinaatu vērtības, lai kuģītis kustētos
        y += vely #pieskaita koordinaatu vērtības, lai kuģītis kustētos

        a.delete("ship") #dzēš kuģīti
        global spongijs
        spongijs = a.create_image(x, y, image = img, tags = 'ship') #izveido kuģīti padarot to kā globas variable


        # logs.after(10, move)
    def key_press(event):
        global pressed_x
        global pressed_y

        global velx
        global vely
        pr = event.char  #pārbauda pogu

        if(pr == "a" ):
            pressed_x='a' #piešķir pressed x vērtībai value, kurš norāda kāda poga pēdējo reizi tika nospiesta
            velx = -1.4
        if(pr == "d"):
            pressed_x='d'
            velx = 1.4
        if(pr == "w"):
            pressed_y='w'
            vely = -1.4
        if(pr == "s"):
            pressed_y='s'
            vely = 1.4
    def key_release(event):
        pr = event.char
        global velx
        global vely
        if pr == 'a' or pr == 'd': # Pārbauda vai viena no atlaistajām pogām ir x ass poga
            velx = 0 #piešķir velx vērtību nulle lai kuģītis nekustās, kad key ir released
        if pr == 'w' or pr == 's':
            vely = 0
        # velx = 0 #piešķir velx vērtību nulle lai kuģītis nekustās, kad key ir released
        # vely = 0
    a.focus_set()
    a.bind("<KeyPress>", key_press)
    a.bind("<KeyRelease>", key_release)



    # KUĢA_ĀTRUMS = 10 

    # def pārvietot_kuģi(notikums): 
    #     if (time()<beigas): #parbauda vai spēle vel notiek
    #         kord = a.coords(spongijs) # Iegūst koordinātes kuģa ārējam aplim
    #         if notikums.keysym == 'Up':
    #             if (kord[1] != 30): # Izveidots if, kas pārbauda vai kuģis nav uz Y ass robežas 
    #                 a.move(spongijs, 0, -KUĢA_ĀTRUMS) 
    #                 # a.move(kuģa_id, 0, -KUĢA_ĀTRUMS) 
    #                 # a.move(kuģa_id2, 0, -KUĢA_ĀTRUMS) 
    #                 # a.move(kuģa_id3, 0, -KUĢA_ĀTRUMS)
    #                 # a.move(kuģa_id4, 0, -KUĢA_ĀTRUMS)
    #         elif notikums.keysym == 'Down': 
    #             if (kord[1] != GARUMS-30): # Izveidots if, kas pārbauda vai kuģis nav uz Y ass robežas 
    #                 a.move(spongijs, 0, KUĢA_ĀTRUMS) 
    #                 # a.move(kuģa_id, 0, KUĢA_ĀTRUMS) 
    #                 # a.move(kuģa_id2, 0, KUĢA_ĀTRUMS) 
    #                 # a.move(kuģa_id3, 0, KUĢA_ĀTRUMS)
    #                 # a.move(kuģa_id4, 0, KUĢA_ĀTRUMS)
    #         elif notikums.keysym == 'Left':  
    #             if (kord[0] != 30): # Izveidots if, kas pārbauda vai kuģis nav uz X ass robežas
    #                 a.move(spongijs, -KUĢA_ĀTRUMS, 0) 
    #                 # a.move(kuģa_id, -KUĢA_ĀTRUMS, 0) 
    #                 # a.move(kuģa_id2, -KUĢA_ĀTRUMS, 0)
    #                 # a.move(kuģa_id3, -KUĢA_ĀTRUMS, 0)
    #                 # a.move(kuģa_id4, -KUĢA_ĀTRUMS, 0)
    #         elif notikums.keysym == 'Right': 
    #             if (kord[0] != PLATUMS-30): # Izveidots if, kas pārbauda vai kuģis nav uz X ass robežas
    #                 a.move(spongijs, KUĢA_ĀTRUMS, 0) 
    #                 # a.move(kuģa_id, KUĢA_ĀTRUMS, 0) 
    #                 # a.move(kuģa_id2, KUĢA_ĀTRUMS, 0) 
    #                 # a.move(kuģa_id3, KUĢA_ĀTRUMS, 0)
    #                 # a.move(kuģa_id4, KUĢA_ĀTRUMS, 0)
    # a.bind_all('<Key>', pārvietot_kuģi)


    burbuļa_id = []
    burbuļa_rādiuss = []
    burbuļa_ātrums = []

    ATSTARPE=100

    # global LIVES
    # LIVES = 3 
    # MIN_BURBUĻA_RĀDIUSS=10 
    # MAX_BURBUĻA_RĀDIUSS=50 
    # MAX_BURBUĻA_ĀTRUMS=40 #max burbuļa ātrumu palielina
    # MIN_ENEMY_RĀDIUSS=40 
    # MAX_ENEMY_RĀDIUSS=50 
    # MAX_ENEMY_ĀTRUMS=15 
    # MIN_BURBUĻA_ĀTRUMS=10


    burbuļu_bildes = [] #izveido jaunu, tukšu listu priekš burbuļa bildēm
    burbuļa_stāvoklis = [] #lists, kurā glabāsies vertiba, vai burbulis ir bīstams vai nē (medūza vai burgers)

    def izveidot_burbuli (stavoklis):
        if stavoklis == 'safe':
            x= PLATUMS+ATSTARPE
            r=randint(MIN_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_RĀDIUSS)
            y=randint(0+r+2, GARUMS-r-5) # pieskaita burbuļa radiusu un 2 un 5, lai burbuļi būtu frame robežās

            # burbulis = a.create_oval(x-r, y-r, x+r, y+r, outline='white') 

            resized_image= burger_img.resize((r,r), Image.Resampling.LANCZOS) #maina bildes izmērus
            new_image = ImageTk.PhotoImage(resized_image) #izveido bildi
            bubble = a.create_image(x,y, image = new_image) #bildi pievieno canvas

            burbuļu_bildes.append(new_image) #pievienu katra burbuļa bildi listam

            burbuļa_id.append(bubble)
            if r>60:
                r = r-20
            if r>50:
                r=r-20
            burbuļa_rādiuss.append(r)
            burbuļa_ātrums.append((randint(MIN_BURBUĻA_ĀTRUMS, MAX_BURBUĻA_ĀTRUMS))/100) #ātrums dalīts ar 100 lai burbuļi ir lēnāki
            burbuļa_stāvoklis.append(stavoklis)


        else:
            x= PLATUMS+ATSTARPE
            r=randint(MIN_ENEMY_RĀDIUSS, MAX_ENEMY_RĀDIUSS)
            y=randint(0+r+2, GARUMS-r-5) # pieskaita burbuļa radiusu un 2 un 5, lai burbuļi būtu frame robežās

            resized_image= enemy_img.resize((r,r), Image.Resampling.LANCZOS) #maina bildes izmērus
            new_image = ImageTk.PhotoImage(resized_image) #izveido bildi
            enemy = a.create_image(x,y, image = new_image) #bildi pievieno canvas

            burbuļu_bildes.append(new_image) #pievienu katra burbuļa bildi listam

            burbuļa_id.append(enemy)
            if r>60:
                r = r-20
            if r>50:
                r=r-20

            burbuļa_rādiuss.append(r)
            burbuļa_ātrums.append((randint(MIN_ENEMY_ĀTRUMS, MAX_ENEMY_ĀTRUMS))/100) #ātrums dalīts ar 100 lai medūzas ir lēnāki
            burbuļa_stāvoklis.append(stavoklis)



    def pārvietot_burbuļus():
        for i in range(len(burbuļa_id)):
            a.move(burbuļa_id[i], -burbuļa_ātrums[i], 0)


    def iegūt_koordinātes(id_skaitlis):
        pozīcija = a.coords(id_skaitlis)
        if len(pozīcija) == 2: #pārbauda vai jāiegūst bildes koordinātas
            x = pozīcija[0]
            y = pozīcija[1]
        elif pozīcija == 0:
            x = (pozīcija[0]+pozīcija[2])/2
            y = (pozīcija[1]+pozīcija[3])/2
        else:
            x,y=0,0

        return x,y

    def dzēst_burbuli(i):
        del burbuļa_rādiuss[i]
        del burbuļa_ātrums[i]
        a.delete(burbuļa_id[i])
        del burbuļa_id[i]
        del burbuļu_bildes[i] #dzēš bildes, kas tika saglabātas veidojot burbuli
        del burbuļa_stāvoklis[i] #dzēš vertības, kas tika saglabātas veidojot burbuli

    def notīrīt_burbuļus():
        for i in range(len(burbuļa_id)-1, -1, -1):
            x,y=iegūt_koordinātes(burbuļa_id[i])
            if x< -ATSTARPE:
                dzēst_burbuli(i)

    def attālums(id1, id2):
        x1, y1 = iegūt_koordinātes(id1)
        x2, y2 = iegūt_koordinātes(id2)
        return sqrt((x2-x1)**2+(y2-y1)**2)

    def sadursme():
        punkti = 0
        for burbulis in range(len(burbuļa_id) -1, -1, -1):
            temp = 0
            if burbuļa_rādiuss[burbulis]>40:
                temp = 5
            if attālums(spongijs, burbuļa_id[burbulis]) < (KUĢA_RĀDIUSS+burbuļa_rādiuss[burbulis]+temp): #mainīts variable name, spongijs, kas kuģīša vietā
                if burbuļa_stāvoklis[burbulis] == 'safe':
                    punkti+= (burbuļa_rādiuss[burbulis]+int(burbuļa_ātrums[burbulis]*100)) #reizina ar 100 lai iegūtu attiecīgu burbuļa ātrumu un pārveido par int
                    dzēst_burbuli(burbulis)
                else:
                    global LIVES
                    LIVES = LIVES - 1
                    dzēst_burbuli(burbulis)

        return punkti


    a.create_text(50, 30, text='LAIKS', fill='white')
    a.create_text(150, 30, text='REZULTĀTS', fill='white')
    laiks_teksts=a.create_text(50, 50, fill='white')
    rezultats_teksts=a.create_text(150, 50, fill='white')


    def parādīt_rezultātu(rezultāts):
        a.itemconfig(rezultats_teksts, text=str(rezultāts))

    def parādīt_laiku(laiks_palicis):
        a.itemconfig(laiks_teksts, text=str(laiks_palicis))

    def show_lives():
        a.delete("sirds")
        y = 750
        for i in range (LIVES): #izvada tik daudz sirdis, cik ir dzīvību
            y-=50
            a.create_image(y, 50, image = lives_img, tags = 'sirds') #Izvada sirdi uz ekrāna


    # BURBUĻI_NEJAUŠI = 40
    # LAIKA_IEROBEŽOJUMS=30
    # PAPILDLAIKA_REZULTĀTS=1000
    # papildu = 0

    beigas = time() + LAIKA_IEROBEŽOJUMS
    rezultāts = 0



    while time()<beigas and LIVES != 0:
        if randint(1, BURBUĻI_NEJAUŠI) == 1:
            if randint(1, BURBUĻI_NEJAUŠI) == 1: #burbuļu izveidošana ielikta divos if statmentos veidojot, lai ir mazāk burbuļu
                izveidot_burbuli('safe')
            if randint(1, ENEMY_NEJAUŠI) == 1: #burbuļu izveidošana ielikta divos if statmentos veidojot, lai ir mazāk burbuļu
                izveidot_burbuli('danger')
                # time = parādīt_dzīvības(time())
        show_lives()
        move()
        pārvietot_burbuļus()
        notīrīt_burbuļus()
        rezultāts+=sadursme()
        # if (int(rezultāts/PAPILDLAIKA_REZULTĀTS))>papildu:
        #     papildu+=1
        #     beigas+=LAIKA_IEROBEŽOJUMS
        parādīt_rezultātu(rezultāts)
        parādīt_laiku(int(beigas-time()))
        if rezultāts >= NEEDED_SCORE:
            break
        logs.update()

    global w
    w = Button ( a,  command=lambda: game.return_back(), text='atgriezties')

    if rezultāts < NEEDED_SCORE:
        a.delete('all')
        a.create_text(VID_X, VID_Y, \
                      text='SPĒLES BEIGAS', fill='white', font=('Helvetica', 30))

        a.create_text(VID_X, VID_Y+30, \
                      text='Rezultāts:' + str(rezultāts), fill='white')



        a.create_text(VID_X, VID_Y+45, \
                      text='Nepieciešamais rezultāts:' + str(NEEDED_SCORE), fill='white')

        w.place(x=370, y=350)
    else:

        a.delete('all')
        a.create_text(VID_X, VID_Y, \
                      text='SPĒLES BEIGAS', fill='white', font=('Helvetica', 30))

        a.create_text(VID_X, VID_Y+30, \
                      text='Rezultāts:' + str(rezultāts), fill='white')

        a.create_text(VID_X, VID_Y+45, \
                      text='TU UZVARĒJI!!' , fill='white')

        w = Button ( a,  command=lambda: game.star_get(level, int(beigas-time())), text='atgriezties')
        w.place(x=370, y=350)
        # game.star_get(level, time)


class Mājas: #izveidota klase mājas
    def __init__(self, bilde, bilde1, bilde2, bilde3, bilde4, bilde5, star, star2): #konstruktorā tiek definēti mainīgie
        self.bilde = bilde
        self.bilde1 = bilde1
        self.bilde2 = bilde2
        self.bilde3 = bilde3
        self.bilde4 = bilde4
        self.bilde5 = bilde5

        self.black_star = star
        self.yellow_star = star2

        self.level1_stars = 0
        self.level2_stars = 0
        self.level3_stars = 0
        self.level4_stars = 0
        self.level5_stars = 0

        Mājas.placer(self)


    def placer(self): #šī funkcija uz ekrāna izvada visu ko satur šis logs
        fonss = a.create_image(380,252, image = self.bilde)  #importo fonu un izveido bildi
        self.poga1 = Button(a,image=self.bilde1, command=lambda: Mājas.sakt_limeni(self, 1),background='#1a2941', activebackground='#1a2941', bd=0)
        self.poga2 = Button(a,image=self.bilde2, command=lambda: Mājas.sakt_limeni(self, 2),background='#1a2941', activebackground='#1a2941', bd=0)
        self.poga3 = Button(a,image=self.bilde3, command=lambda: Mājas.sakt_limeni(self, 3),background='#1a2941', activebackground='#1a2941', bd=0)
        self.poga4 = Button(a,image=self.bilde4, command=lambda: Mājas.sakt_limeni(self, 4),background='#1a2941', activebackground='#1a2941', bd=0)
        self.poga5 = Button(a,image=self.bilde5, command=lambda: Mājas.sakt_limeni(self, 5),background='#1a2941', activebackground='#1a2941', bd=0)
        self.poga1.place(x=180, y=92)
        self.poga2.place(x=328, y=92)
        self.poga3.place(x=471, y=92)
        self.poga4.place(x=610, y=92)
        self.poga5.place(x=613, y=218)

        if self.level1_stars == 3: #pārbauda zvaigžņu skaitu
            a.create_image(205,200, image = self.yellow_star, tags = 'star')
            a.create_image(235,200, image = self.yellow_star, tags = 'star')
            a.create_image(265,200, image = self.yellow_star, tags = 'star')
        elif self.level1_stars == 2:
            a.create_image(205,200, image = self.yellow_star, tags = 'star')
            a.create_image(235,200, image = self.yellow_star, tags = 'star')
            a.create_image(265,200, image = self.black_star, tags = 'star')

        elif self.level1_stars == 1:
            a.create_image(205,200, image = self.yellow_star, tags = 'star')
            a.create_image(235,200, image = self.black_star, tags = 'star')
            a.create_image(265,200, image = self.black_star, tags = 'star')
        else:
            a.create_image(205,200, image = self.black_star, tags = 'star')
            a.create_image(235,200, image = self.black_star, tags = 'star')
            a.create_image(265,200, image = self.black_star, tags = 'star')



        if self.level2_stars == 3:
            a.create_image(355,200, image = self.yellow_star, tags = 'star')
            a.create_image(385,200, image = self.yellow_star, tags = 'star')
            a.create_image(415,200, image = self.yellow_star, tags = 'star')
        elif self.level2_stars == 2:
            a.create_image(355,200, image = self.yellow_star, tags = 'star')
            a.create_image(385,200, image = self.yellow_star, tags = 'star')
            a.create_image(415,200, image = self.black_star, tags = 'star')

        elif self.level2_stars == 1:
            a.create_image(355,200, image = self.yellow_star, tags = 'star')
            a.create_image(385,200, image = self.black_star, tags = 'star')
            a.create_image(415,200, image = self.black_star, tags = 'star')
        else:
            a.create_image(355,200, image = self.black_star, tags = 'star')
            a.create_image(385,200, image = self.black_star, tags = 'star')
            a.create_image(415,200, image = self.black_star, tags = 'star')


        if self.level3_stars == 3:
            a.create_image(495,200, image = self.yellow_star, tags = 'star')
            a.create_image(525,200, image = self.yellow_star, tags = 'star')
            a.create_image(555,200, image = self.yellow_star, tags = 'star')
        elif self.level3_stars == 2:
            a.create_image(495,200, image = self.yellow_star, tags = 'star')
            a.create_image(525,200, image = self.yellow_star, tags = 'star')
            a.create_image(555,200, image = self.black_star, tags = 'star')

        elif self.level3_stars == 1:
            a.create_image(495,200, image = self.yellow_star, tags = 'star')
            a.create_image(525,200, image = self.black_star, tags = 'star')
            a.create_image(555,200, image = self.black_star, tags = 'star')
        else:
            a.create_image(495,200, image = self.black_star, tags = 'star')
            a.create_image(525,200, image = self.black_star, tags = 'star')
            a.create_image(555,200, image = self.black_star, tags = 'star')

        if self.level4_stars == 3:
            a.create_image(640,200, image = self.yellow_star, tags = 'star')
            a.create_image(670,200, image = self.yellow_star, tags = 'star')
            a.create_image(700,200, image = self.yellow_star, tags = 'star')
        elif self.level4_stars == 2:
            a.create_image(640,200, image = self.yellow_star, tags = 'star')
            a.create_image(670,200, image = self.yellow_star, tags = 'star')
            a.create_image(700,200, image = self.black_star, tags = 'star')

        elif self.level4_stars == 1:
            a.create_image(640,200, image = self.yellow_star, tags = 'star')
            a.create_image(670,200, image = self.black_star, tags = 'star')
            a.create_image(700,200, image = self.black_star, tags = 'star')
        else:
            a.create_image(640,200, image = self.black_star, tags = 'star')
            a.create_image(670,200, image = self.black_star, tags = 'star')
            a.create_image(700,200, image = self.black_star, tags = 'star')

        if self.level5_stars == 3:
            a.create_image(640,324, image = self.yellow_star, tags = 'star')
            a.create_image(670,324, image = self.yellow_star, tags = 'star')
            a.create_image(700,324, image = self.yellow_star, tags = 'star')
        elif self.level5_stars == 2:
            a.create_image(640,324, image = self.yellow_star, tags = 'star')
            a.create_image(670,324, image = self.yellow_star, tags = 'star')
            a.create_image(700,324, image = self.black_star, tags = 'star')

        elif self.level5_stars == 1:
            a.create_image(640,324, image = self.yellow_star, tags = 'star')
            a.create_image(670,324, image = self.black_star, tags = 'star')
            a.create_image(700,324, image = self.black_star, tags = 'star')
        else:
            a.create_image(640,324, image = self.black_star, tags = 'star')
            a.create_image(670,324, image = self.black_star, tags = 'star')
            a.create_image(700,324, image = self.black_star, tags = 'star')


        # yellow_star = a.create_image(50,50, image = self.yellow_star, tags = 'star')  #importo spengebob un izveido bildi



    def sakt_limeni(self, limenis): #līmeņa uzsākšanas funkcija
        global LIVES
        if limenis == 1:

            LIVES = 5
            level = 1


            BURBUĻI_NEJAUŠI = 15
            ENEMY_NEJAUŠI = 100

            LAIKA_IEROBEŽOJUMS=60
            MIN_BURBUĻA_RĀDIUSS=20
            MAX_BURBUĻA_RĀDIUSS=60

            MAX_BURBUĻA_ĀTRUMS=40 #max burbuļa ātrumu palielina
            MIN_BURBUĻA_ĀTRUMS=40

            MIN_ENEMY_RĀDIUSS=20
            MAX_ENEMY_RĀDIUSS=40
            MIN_ENEMY_ĀTRUMS = 10
            MAX_ENEMY_ĀTRUMS=15

            NEEDED_SCORE = 2000

            a.delete('all')
            self.poga1.destroy()
            self.poga2.destroy()
            self.poga3.destroy()
            self.poga4.destroy()
            self.poga5.destroy()

            fona_bilde = PhotoImage(file = 'pirmkods/fons1.png')  #izveidota fona bilde

            start_game(level, BURBUĻI_NEJAUŠI, ENEMY_NEJAUŠI, LAIKA_IEROBEŽOJUMS, MIN_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_ĀTRUMS, MIN_BURBUĻA_ĀTRUMS, MIN_ENEMY_RĀDIUSS, MAX_ENEMY_RĀDIUSS, MIN_ENEMY_ĀTRUMS, MAX_ENEMY_ĀTRUMS, fona_bilde, NEEDED_SCORE) #tiek izsaukta galvenā spēle 

        if limenis == 2:

            LIVES = 4
            level = 2

            BURBUĻI_NEJAUŠI = 15
            ENEMY_NEJAUŠI = 45

            LAIKA_IEROBEŽOJUMS=60
            MIN_BURBUĻA_RĀDIUSS=20
            MAX_BURBUĻA_RĀDIUSS=50

            MAX_BURBUĻA_ĀTRUMS=80 #max burbuļa ātrumu palielina
            MIN_BURBUĻA_ĀTRUMS=30

            MIN_ENEMY_RĀDIUSS=40
            MAX_ENEMY_RĀDIUSS=90
            MIN_ENEMY_ĀTRUMS = 10
            MAX_ENEMY_ĀTRUMS=90

            NEEDED_SCORE = 2000

            a.delete('all')
            self.poga1.destroy()
            self.poga2.destroy()
            self.poga3.destroy()
            self.poga4.destroy()
            self.poga5.destroy()

            fona_bilde = PhotoImage(file = 'pirmkods/fons2.png')

            start_game(level, BURBUĻI_NEJAUŠI, ENEMY_NEJAUŠI, LAIKA_IEROBEŽOJUMS, MIN_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_ĀTRUMS, MIN_BURBUĻA_ĀTRUMS, MIN_ENEMY_RĀDIUSS, MAX_ENEMY_RĀDIUSS, MIN_ENEMY_ĀTRUMS, MAX_ENEMY_ĀTRUMS, fona_bilde, NEEDED_SCORE)

        if limenis == 3:

            LIVES = 3
            level = 3

            BURBUĻI_NEJAUŠI = 20
            ENEMY_NEJAUŠI = 13

            LAIKA_IEROBEŽOJUMS=60
            MIN_BURBUĻA_RĀDIUSS=20
            MAX_BURBUĻA_RĀDIUSS=70

            MAX_BURBUĻA_ĀTRUMS=120 #max burbuļa ātrumu palielina
            MIN_BURBUĻA_ĀTRUMS=40

            MIN_ENEMY_RĀDIUSS=50
            MAX_ENEMY_RĀDIUSS=80

            MIN_ENEMY_ĀTRUMS = 15
            MAX_ENEMY_ĀTRUMS=45

            NEEDED_SCORE = 2500

            a.delete('all')
            self.poga1.destroy()
            self.poga2.destroy()
            self.poga3.destroy()
            self.poga4.destroy()
            self.poga5.destroy()

            fona_bilde = PhotoImage(file = 'pirmkods/fons3.png')

            start_game(level, BURBUĻI_NEJAUŠI, ENEMY_NEJAUŠI, LAIKA_IEROBEŽOJUMS, MIN_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_ĀTRUMS, MIN_BURBUĻA_ĀTRUMS, MIN_ENEMY_RĀDIUSS, MAX_ENEMY_RĀDIUSS, MIN_ENEMY_ĀTRUMS, MAX_ENEMY_ĀTRUMS, fona_bilde, NEEDED_SCORE)


        if limenis == 4:

            LIVES = 2
            level = 4

            BURBUĻI_NEJAUŠI = 10
            ENEMY_NEJAUŠI = 20

            LAIKA_IEROBEŽOJUMS=60
            MIN_BURBUĻA_RĀDIUSS=10
            MAX_BURBUĻA_RĀDIUSS=15

            MAX_BURBUĻA_ĀTRUMS=70 #max burbuļa ātrumu palielina
            MIN_BURBUĻA_ĀTRUMS=40

            MIN_ENEMY_RĀDIUSS=40
            MAX_ENEMY_RĀDIUSS=40
            MIN_ENEMY_ĀTRUMS = 35
            MAX_ENEMY_ĀTRUMS=55

            NEEDED_SCORE = 2000

            a.delete('all')
            self.poga1.destroy()
            self.poga2.destroy()
            self.poga3.destroy()
            self.poga4.destroy()
            self.poga5.destroy()

            fona_bilde = PhotoImage(file = 'pirmkods/fons4.png')

            start_game(level, BURBUĻI_NEJAUŠI, ENEMY_NEJAUŠI, LAIKA_IEROBEŽOJUMS, MIN_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_ĀTRUMS, MIN_BURBUĻA_ĀTRUMS, MIN_ENEMY_RĀDIUSS, MAX_ENEMY_RĀDIUSS, MIN_ENEMY_ĀTRUMS, MAX_ENEMY_ĀTRUMS, fona_bilde, NEEDED_SCORE)


        if limenis == 5:

            LIVES = 1
            level = 5

            BURBUĻI_NEJAUŠI = 10
            ENEMY_NEJAUŠI = 5

            LAIKA_IEROBEŽOJUMS=60
            MIN_BURBUĻA_RĀDIUSS=20
            MAX_BURBUĻA_RĀDIUSS=30

            MAX_BURBUĻA_ĀTRUMS=180 #max burbuļa ātrumu palielina
            MIN_BURBUĻA_ĀTRUMS=80

            MIN_ENEMY_RĀDIUSS=40
            MAX_ENEMY_RĀDIUSS=40
            MIN_ENEMY_ĀTRUMS = 75
            MAX_ENEMY_ĀTRUMS=165

            a.delete('all')
            self.poga1.destroy()
            self.poga2.destroy()
            self.poga3.destroy()
            self.poga4.destroy()
            self.poga5.destroy()

            NEEDED_SCORE = 4000

            fona_bilde = PhotoImage(file = 'pirmkods/fons5.png')

            start_game(level, BURBUĻI_NEJAUŠI, ENEMY_NEJAUŠI, LAIKA_IEROBEŽOJUMS, MIN_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_RĀDIUSS, MAX_BURBUĻA_ĀTRUMS, MIN_BURBUĻA_ĀTRUMS, MIN_ENEMY_RĀDIUSS, MAX_ENEMY_RĀDIUSS, MIN_ENEMY_ĀTRUMS, MAX_ENEMY_ĀTRUMS, fona_bilde, NEEDED_SCORE)



    def return_back(self):


        w.destroy()
        Mājas.star_get(self)


    def star_get(self, level = 0, time = 0):
        w.destroy()
        a.delete('all')

        if level == 1:
            if LIVES == 5 and time>27:
                self.level1_stars = 3
            elif LIVES >= 4:
                self.level1_stars = 2
            elif LIVES > 0 and time>0:
                self.level1_stars=1

        if level == 2:
            if LIVES == 4 and time>20:
                self.level2_stars = 3
            elif LIVES >= 3:
                self.level2_stars = 2
            elif LIVES > 0 and time>0:
                self.level2_stars=1

        if level == 3:
            if LIVES == 3 and time>20:
                self.level3_stars = 3
            elif LIVES >= 2:
                self.level3_stars = 2
            elif LIVES > 0 and time>0:
                self.level3_stars=1

        if level == 4:
            if LIVES == 2 and time>20:
                self.level4_stars = 3
            elif LIVES >= 1:
                self.level4_stars = 2
            elif LIVES > 0 and time>0:
                self.level4_stars=1

        if level == 5:
            if LIVES == 1 and time>20:
                self.level5_stars = 3
            elif LIVES == 1 and time>10:
                self.level5_stars = 2
            elif LIVES > 0 and time>0:
                self.level5_stars=1



        Mājas.placer(self)







start_fona_bilde = PhotoImage(file = 'pirmkods/levels.png')
level1 = ImageTk.PhotoImage(Image.open("pirmkods/level1.png"))
level2 = ImageTk.PhotoImage(Image.open("pirmkods/level2.png"))
level3 = ImageTk.PhotoImage(Image.open("pirmkods/level3.png"))
level4 = ImageTk.PhotoImage(Image.open("pirmkods/level4.png"))
level5 = ImageTk.PhotoImage(Image.open("pirmkods/level5.png"))

star1 = ImageTk.PhotoImage(Image.open("pirmkods/black_star.png"))
star2 = ImageTk.PhotoImage(Image.open("pirmkods/star.png"))

game = Mājas(start_fona_bilde, level1, level2, level3, level4, level5, star1, star2)

# start_game()

mainloop()