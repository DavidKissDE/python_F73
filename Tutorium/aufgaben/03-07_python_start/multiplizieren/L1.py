#%
# zwei Ganzzahlen einzugeben.
# ungültige Eingaben abfangen
# multipliziert mittels Addition

while True:
      try: 
            x = round(float(input("Erste Zahl: ")))
            y = round(float(input("Zweite Zahl: ")))
            break
      except:
            pass

result = 0
for _ in range(abs(x)):
      result+=y
if x<0:
      result=-result

print(result)
