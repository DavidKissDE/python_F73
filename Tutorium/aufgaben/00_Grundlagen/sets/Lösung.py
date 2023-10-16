#%
A = {1,2,3,4}
B = {4}
B.add(5)

print( 6 in B)

#%
print( A.intersection(B) )
print( A.union(B) )
print( A.difference(B) )

#%
def unique_simple(some_list: list) -> list:
      return list(set(some_list))

my_list = [5,1,1,1,2,3]
print( unique_simple(my_list) )

def unique(some_list: list) -> list:
      result = []
      for x in some_list:
            if x not in result:
                  result.append(x) 
      return result

print( unique(my_list) )
