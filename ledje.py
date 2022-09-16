from time import sleep #importeer sleep van de libary time
from gpiozero import LED #importeer LED van de libary gpiozero

varLedr = LED(1) #varLedr is aangesloten op GPIO1
varLedb = LED(2) #varLedb is aangesloten op GPIO2
varLedg = LED(3) #varLedg is aangesloten op GPIO3
while True: #zolang de status true is dan
    varLedr.off() #stuur het rode ledje uit
    varLedg.off() #stuur het groene ledje uit
    varLedb.off() #stuur het blauwe ledje uit
    sleep(0.2) #wacht 200 millie seconden
    varLedr.off() #stuur het rode ledje uit
    varLedg.off() #stuur het groene ledje uit
    varLedb.on() #stuur het blauwe ledje aan
    sleep(0.2) #wacht 200 millie seconden
    varLedr.off() #stuur het rode ledje uit
    varLedg.on() #stuur het groene ledje aan
    varLedb.off() #stuur het blauwe ledje uit
    sleep(0.2) #wacht 200 millie seconden
    varLedr.off() #stuur het rode ledje uit
    varLedg.on() #stuur het groene ledje aan
    varLedb.on() #stuur het blauwe ledje aan
    sleep(0.2) #wacht 200 millie seconden
    varLedr.on() #stuur het rode ledje aan
    varLedg.off() #stuur het groene ledje uit
    varLedb.off() #stuur het blauwe ledje uit
    sleep(0.2) #wacht 200 millie seconden
    varLedr.on() #stuur het rode ledje aan
    varLedg.off() #stuur het groene ledje uit
    varLedb.on() #stuur het blauwe ledje aan
    sleep(0.2) #wacht 200 millie seconden
    varLedr.on() #stuur het rode ledje aan
    varLedg.on() #stuur het groene ledje aan
    varLedb.off() #stuur het blauwe ledje uit
    sleep(0.2) #wacht 200 millie seconden
    varLedr.on() #stuur het rode ledje aan
    varLedg.on() #stuur het groene ledje aan
    varLedb.on() #stuur het blauwe ledje aan
    sleep(0.2) #wacht 200 millie seconden