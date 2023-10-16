print('Lottozahlengenerator')
 
from random import randint
 
result = []
 
 
zahl1 = randint(1, 49)
 
zahl2 = randint(1, 49)
while zahl2 == zahl1:
    zahl2 = randint(1, 49)
 
zahl3 = randint(1, 49)
while (zahl3 == zahl1) or (zahl3 == zahl2):
    zahl3 = randint(1,49)
 
zahl4 = randint(1, 49)
while (zahl4 == zahl1) or (zahl4 == zahl2) or (zahl4 == zahl3):
    zahl4 = randint(1, 49)
 
zahl5 = randint(1, 49)
while (zahl5 == zahl1) or (zahl5 == zahl2) or (zahl5 == zahl3) or (zahl5 == zahl4):
    zahl5 = randint(1, 49)
 
zahl6 = randint(1,49)
while (zahl6 == zahl1) or (zahl6 == zahl2) or (zahl6 == zahl3) or (zahl6 == zahl4) or (zahl6 == zahl5):
    zahl6 = randint(1, 49)
 
 
result.append(zahl1)
result.append(zahl2)
result.append(zahl3)
result.append(zahl4)
result.append(zahl5)
result.append(zahl6)
result.sort()

print(result)