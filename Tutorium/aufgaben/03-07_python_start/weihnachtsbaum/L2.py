hoehe = int(input("Wie viele Zeilen hoch soll der Weinachtsbaum sein? "))
basis = [1, 3, 5]
zeichen = "*"
x = hoehe // 3

# Durchläuft Anzahl dreier Blöcke
for i in range(0, x):
    for b in basis:
        # Ausgabe damit der Tannenbaum immer angepasst wird
        print((zeichen * (b + (i * 2))).center(5 + (x * 2)))

# Ausgabe Stamm
print("###".center(5 + (x * 2)))
