# Palindrome (mit Listen)

* Schreibe eine Python-Funktion mit dem Namen `find_palindrome_list`, die eine Liste von Zeichenketten als Argument nimmt und eine neue Liste zurückgibt, die nur die Palindrome enthält. 
    * Ein __Palindrom__ ist ein Wort, das von vorne und von hinten gelesen gleich ist. 
* Die Rückgabeliste soll keine Duplikate enthalten und die Elemente sollten in der gleichen Reihenfolge wie in der ursprünglichen Liste vorkommen.

Hier ist ein Beispiel, wie die Funktion verwendet werden sollte:

``` python
>>> find_palindrome_list(['radar', 'anna', 'level', 'hello', 'world'])
['radar', 'anna', 'level']
>>> find_palindrome_list(['rotor', 'madam', 'civic'])
['rotor', 'madam', 'civic']
>>> find_palindrome_list(['hello', 'world'])
[]
```


# Aufgabe 7 - Palindrome (mit Strings)

Schwierigkeitsgrad: 30/100

Programmierkonzepte: functions, variables, lists, loops, tring manipulation and reversing strings

Schreibe eine Python-Funktion mit dem Namen *find_palindrome_str*, die eine Zeichenkette als Argument nimmt und eine neue Zeichenkette zurückgibt, die nur die Palindrome enthält. Ein Palindrom ist ein Wort, das von vorne und von hinten gelesen gleich ist. Die Rückgabezeichenkette soll keine Duplikate enthalten und die Elemente sollten in der gleichen Reihenfolge wie in der ursprünglichen Zeichenkette vorkommen.

Hier ist ein Beispiel, wie die Funktion verwendet werden sollte:

``` python
>>> find_palindrome_str('radarannalevelhello world')
'radarannalevel'
>>> find_palindrome_str('rotormadamcivic')
'rotormadamcivic'
>>> find_palindrome_str('hello world')
''
```