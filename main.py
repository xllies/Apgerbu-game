from tkinter import *

GARUMS = 558
PLATUMS = 864
logs = Tk()
logs.title('Ko vilkt?')

a = Canvas(logs, width=PLATUMS, height=GARUMS, bg='#4b6fa6') 
a.pack()

fona_bilde = PhotoImage(file = 'pirmkods/fons3.png')
fons = a.create_image(402,252, image = fona_bilde)  #importo fonu un izveido bildi
