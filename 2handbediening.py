import time#importeer tijd
from gpiozero import LED #importeer LED van de libary gpiozero
from gpiozero import Button #importeer LED van de libary gpiozero


varLedg = LED(3) #varLed is aangesloten op GPIO3
button5 = Button(1, pull_up = False) #button5 is aangesloten op pin 1 en is een pull_down weerstand
button6 = Button(5 , pull_up = False) #button6 is aangesloten op pin 5 en is een pull_down weerstand

interval = 1#interval is gelijk aan 1
starttime = 0#de starttijd is gelijk aan 0
stoptime = 0# de stopstijd is gelijk aan 0

varLedg.off() #stuur het ledje uit 
while True: #zolang de status true is dan  
    if button5.value == False or button6.value == False:# als button5 laag is of button 6 dan
        stoptime = starttime# stel de stoptijd gelijk aan de starttijd
        varLedg.off() #stuur het ledje uit 
    if button6.value == True or button5.value == True:# als button5 hoog is of button 6 dan
        starttime = time.time()#stel de startijd gelijk aan de timer
        if button5.value and button6.value:# als button5 hoog is en button 6 dan
            stoptime = time.time() #stel de stoptijd gelijk aan de timer
            if (stoptime - starttime) < interval: #als de stoptijd -de starttijd kleiner is dan de interval dan
                varLedg.on() #stuur het ledje aan
        