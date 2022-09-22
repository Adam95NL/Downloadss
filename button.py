from time import sleep #importeer sleep van de libary time
from gpiozero import LED #importeer LED van de libary gpiozero
from gpiozero import Button #importeer LED van de libary gpiozero


varLedg = LED(3) #varLed is aangesloten op GPIO18
button = Button(1, pull_up = False) #button is aangesloten op pin 1 en is een pull_down weerstand
variable = 0 #variable is gelijk aan 0
lastbuttonstate = 0# last buttonstate is gelijk aan 0

while True: #zolang de status true is dan
    if button.value != lastbuttonstate:# als de button.value niet gelijk is aan de vorige buttonstate is dan
        if button.value == True:# als de button.value hoog is dan 
            if variable == 1:#als de variable gelijk is aan 1 dan
                varLedg.off() #stuur het ledje uit  
                variable = 0 #maak variable gelijk aan 0
                sleep(0.2) #wacht 0.2 seconden
            else: # anders 
                varLedg.on() #stuur het ledje aan      
                variable = 1 #maak variable gelijk aan 1
                sleep(0.2) #wacht 0.2 seconden
        lastbuttonstate = button.value #maak de vorige buttonstate gelijk aan de button.value

    
    
        