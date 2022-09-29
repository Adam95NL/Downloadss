from gpiozero import LED #importeer LED van de libary gpiozero
from gpiozero import Button #importeer Button van de libary gpiozero
varLedr = LED(11) #varLedr is aangesloten op GPIO11
varLedb = LED(2) #varLedb is aangesloten op GPIO2
varLedg = LED(3) #varLedg is aangesloten op GPIO3
button1 = Button(5, pull_up = False) #button1 is aangesloten op gpio 5 en is een pull_down weerstand
button2 = Button(6, pull_up = False) #button2 is aangesloten op gpio 6 en is een pull_down weerstand
while True: #zolang de status true is dan
    if button1.value == True and button2.value == True:# als de button1.value hoog is en button2.value hoog is dan
        varLedr.on() #stuur het rode ledje aan    
        varLedg.on() #stuur het groene ledje aan   
        varLedb.on() #stuur het blauwe ledje aan  
    if button1.value == True and button2.value == False:# als de button1.value hoog is en button2.value laag is dan
        varLedr.on() #stuur het rode ledje aan     
        varLedg.off() #stuur het groene ledje uit   
        varLedb.off() #stuur het blauwe ledje uit  
    if button1.value == False and button2.value == True:# als de button1.value laag is en button2.value hoog is dan
        varLedr.off() #stuur het rode ledje uit    
        varLedg.on() #stuur het groene ledje aan   
        varLedb.off() #stuur het blauwe ledje uit  
    else: #als geen van de bovenste combinaties worden bediend dan
        varLedr.off() #stuur het rode ledje uit    
        varLedg.off() #stuur het groene ledje uit   
        varLedb.off() #stuur het blauwe ledje uit  