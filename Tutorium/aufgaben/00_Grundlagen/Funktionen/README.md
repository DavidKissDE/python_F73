## Funktionen
Implementiere folgende Funktionen:

* `add(x,y)` ermittelt die Summe aus `x` und `y`.
* `square(b)` ermittelt das Quadrat von (der Basis) `b`, bspw. `square(3) = 9`.
* `summe(n)` summiert die Zahlen `1` bis `n` auf.
* `ist_zahl(string)` wertet zu `True` aus, falls sämtliche Zeichen in `string` Zahlen sind, sonst `False`.

### Verschachtelte Funktionen
* Verwende deine Implementierungen von `add` und `square`, um eine Funktion 
    ```
    add_sq(x,y) = x^2 + y^2
    ``` 
    zu implementieren. Ein Bsp.:
    ``` python
    add_sq(2,3) = 2^2 + 3^2 = 4+9 = 13
    ```
* _1. Hinweis_: Die Antwort ist ein Einzeiler.
* _2. Hinweis_: Dies ist ein einfaches Beispiel für _funktionale Programmierung_.

### Docstrings
* Vereinbare die Funktion `greet`, der man Optional einen Namen übergeben kann.
    * Wird ein Name, bspw. "Python",  überreicht, so soll
        ``` 
       Hello Python!
        ```
        ausgegeben werden. 
    * Wird kein Name überreicht, so soll
        ``` 
        Hello Human (or some other Entity)!
        ```
        erscheinen.
* Versehe deine Funktion mit einem Docstring. Ein Beispiel findest du [hier](docstring_example.py).


### map und Lambda-Funktion
* Führe den Befehl
    ``` python
    map(square, [2,3,4])
    ```
    aus und speichere das `map`-Objekt in einer Variable. 
    * Wie könnte man das Ergebnis ausgeben? 
    * Was bewirkt `map` in diesem konkreten Beispiel? 
* Challenge: Ersetze im obigen `map`-Befehl die Funktion `square` durch eine Lambda-Funktion.
    * Was ist eine Lambda Funktion?
    * In welchen Situationen können Lambda-Funktionen nützlich sein?


### Navigation
* Zurück zu [Grundlagen](../README.md)
* Zurück zur [Hauptseite](../../../README.md)
