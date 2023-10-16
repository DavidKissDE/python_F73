#%
# 6 Zahlen zwischen 1 und 49 generiert.
# in sortierter, aufsteigender Reihenfolge ausgegeben.

#%
import random

numbers = set()

while len(numbers) <6:
      numbers.add(random.randint(1, 49))

numbers