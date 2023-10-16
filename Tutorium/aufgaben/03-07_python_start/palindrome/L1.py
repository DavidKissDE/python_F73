#%
"""
>>> find_palindrome_list(['radar', 'anna', 'level', 'hello', 'world'])
['radar', 'anna', 'level']
>>> find_palindrome_list(['rotor', 'madam', 'civic'])
['rotor', 'madam', 'civic']
>>> find_palindrome_list(['hello', 'world'])
[]
"""

lst =['radar', 'anna', 'level', 'hello', 'world', "radar"]
# lst = ['rotor', 'madam', 'civic']
# lst = ['hello', 'world']

def find_palindrome_list(lst):
      palindromes = [word for word in lst if word==word[::-1]]
      palindromes_unique = []
      for word in palindromes:
            if word not in palindromes_unique:
                  palindromes_unique.append(word)
      return palindromes_unique
      
find_palindrome_list(lst)