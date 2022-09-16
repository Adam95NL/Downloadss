from time import sleep #importeer sleep van de libary time
from gpiozero import LED #importeer LED van de libary gpiozero
from gpiozero import Button #importeer LED van de libary gpiozero


varLedg = LED(3) #varLed is aangesloten op GPIO18
button = Button(1, pull_up = False)

while True: #zolang de status true is dan
    if button.value == True:
        varLedg.on() #stuur het ledje aan
    else:
        varLedg.off() #stuur het ledje aan
    
    
        