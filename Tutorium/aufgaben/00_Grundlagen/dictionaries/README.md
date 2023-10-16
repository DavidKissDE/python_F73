## Dictionaries

### Grundlagen
* Erstelle folgendes dictionary
    ```
    my_dict = {"a":9, "b":0}
    ``` 
* Füge den Wert `5` mit Schlüssel `"c"` ein.
* Rufe die Methoden `keys`, `values` und `items` and deinem dictionary auf. Was machen diese?
* Was bewirken die Methoden `pop` sowie `popitem`?

### membership
* Führe den Befehl
    ``` python
    my_dict = {"a":9, "b":0, "c":5}
    ``` 
    aus (dient der Wiederherstellung des ursprünglichen dictionaries).
* Warum erhalten wir
    ``` python
    >>> print( 9 in my_dict)
    False
    ```
    Obwohl `9` im dictionary enthalten ist? Ändere den `print`-Befehl so ab, dass wir das erwartete Ergebnis erhalten.

### 2 Listen, 1 Dictionary!
* Was macht die `zip` Funktion? Mache dich mit ihr vertraut.
* Versuche, `my_dict2` mit Hilfe von `zip` zu erzeugen. Es soll die selben Einträge wie `my_dict` besitzen.

### "get" Methode
* Was genau macht die `get` Methode?
* Durchlaufe die Liste 
    ```
    [("d", 123), ("e", 666), ("e", 999)]
    ```
    und füge die Listen-Elemente in `my_dict` ein. 
    * der Schlüssel `"e"` könnte Probleme bereiten. Finde einen Weg, die Liste mit neuen items ohne Fehler durchlaufen zu können.

### "sorted_dict" Funktion
* Vereinbare die Liste `[9, 0, 5]`. Gebe diese mit Hilfe von `sorted` sortiert aus.
* Vereinbare nun eine Funktion `sorted_dict`, die bspw. das dictionary
    ```
    my_dict = {"a":9, "b":0, "c":5}
    ```
    anhand _seiner Werte_ sortiert.
    * _Tipp_: Diese Aufgabe kann (muss aber selbstverständlich nicht) mit Hilfe einer Lambda-Funktion gelöst werden.

### Navigation
* Zurück zu [Grundlagen](../README.md)
* Zurück zur [Hauptseite](../../../README.md)





