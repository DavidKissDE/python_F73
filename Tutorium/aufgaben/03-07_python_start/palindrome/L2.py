# Um diese Aufgabe zu lösen, kannst du die reversed Funktion verwenden, um das Wort rückwärts 
# zu lesen und es mit dem ursprünglichen Wort zu vergleichen. Du kannst auch die in-Operator 
# verwenden, um zu überprüfen, ob ein Element bereits in der Rückgabeliste enthalten ist, 
# bevor du es hinzufügst.
def find_palindrome_list(words:list):
    palindrome_words = []
    for word in words:
        if word == ''.join(reversed(word)):
            if word not in palindrome_words:
                palindrome_words.append(word)
    return palindrome_words

def find_palindrome_str(string:str):
    palindrome_string = ""
    for word in string.split():
        if word == ''.join(reversed(word)):
            if word not in palindrome_string:
                palindrome_string += word + ' '
    return palindrome_string.rstrip()

