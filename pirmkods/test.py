from tkinter import *

LENGHT = 500
WIDTH = 800
window = Tk()
window.title('Burbuļu spridzinātājs')

a = Canvas(window, width=WIDTH, height=LENGHT, bg = 'red')
a.pack()

background = PhotoImage(file = 'C:/Users/teres/Desktop/Proxlight_Designer_Export/pirmkods/a.png')  
fons = a.create_image(402,110, image = background)

img = PhotoImage(file = 'C:/Users/teres/Desktop/Proxlight_Designer_Export/pirmkods/spongy311.png')  
spongijs = a.create_image(50,50, image = img, tags = 'ship')

KUĢA_RĀDIUSS = 15
VID_X = WIDTH / 2
VID_Y = LENGHT / 2

a.move(spongijs, VID_X, VID_Y)

velx = 0 
vely = 0 
global x
global y
x, y = VID_X, VID_Y 

def move():
    global x
    global y
    global velx
    if x <=30 and pressed_x == 'a':
        velx = 0
    x += velx
    y += vely
    print(x)
    print(y)
    a.delete("ship") 
    global spongijs 
    spongijs = a.create_image(x, y, image = img, tags = 'ship') 


def key_press(event):
    
    global pressed_x
    global velx
    global vely
    pr = event.char  
    kord = a.coords(spongijs) # Iegūst koordinātes kuģa ārējam aplim
    
    if(pr == "a" ):
        pressed_x='a'
        # if x <=30:
        #     velx = 0
        # else:
        
        velx = -0.1
    
            # a.unbind('<KeyPress-a>', i)
            # velx = -0.1
    # if(pr == "a"):     
    #     velx = -0.1
    if(pr == "d"):     
        velx = 0.1
        pressed_x='d'
    if(pr == "w"):
        vely = -0.1
    if(pr == "s"):
        vely = 0.1
def key_release(event):
    global velx
    global vely
    velx = 0
    vely = 0
a.focus_set()
a.bind("<KeyPress>", key_press)
a.bind("<KeyRelease>", key_release)

# a.bind_all('<Key>', move)
while True:
    move()
    window.update()
    