#%
def add(x,y):
      return x+y

print(add(5,3))

#%
def square(b):
      return b**2

print(square(3))

#%
def summe(n):
      if n>=0:
            result = 0
            i = 0
            while i<=n:
                  result += i
                  i+=1
      return result

'''
1     2     3     4     5
1     3     6     10    15
'''

print(summe(4)) 

#%
def ist_zahl(string:str):
      return string.isnumeric()

print(ist_zahl("123a"))

#%
def add_sq(x,y):
      return add( square(x), square(y) )

print(add_sq(2,3))

#%
def greet(name="Human (or some other Entity)"):
      """
      This friendly litte function greets you.

      Parameters
      ----------
      name : str
            The name of the person that's greeted

      Returns
      -------
            None
      """
      print(f"Hello {name}!")

greet()

#%
mp = map(square, [2,3,4])
print( list(mp) )

mp2 = map( lambda x: x**2, [2,3,4] )
print( list(mp2) )
