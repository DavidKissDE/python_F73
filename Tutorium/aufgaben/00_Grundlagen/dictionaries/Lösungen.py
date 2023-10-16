#%    GRUNDLAGEN
my_dict = {"a":9, "b":0}
my_dict["c"] = 5

print( my_dict )

print( my_dict.keys() )
print( my_dict.values() )
print( my_dict.items() )

print( my_dict.pop("a") )
print( my_dict.popitem() )


#%    MEMBERSHIP
my_dict = {"a":9, "b":0, "c":5}
print( 9 in my_dict)
print( 9 in my_dict.values() )


#%    2 LISTEN, 1 DICT
list1 = list(range(1,5))
list2 = list(range(66,70))
print( list(zip(list1, list2)) )

print( dict( zip( ["a","b","c"], [9, 0, 5] ) ) )


#%    GET-METHODE
my_dict = {"a":9, "b":0, "c":5}

for k,v in [("d", 123), ("e", 666), ("e", 999)]:
      if not my_dict.get(k):
            my_dict[k] = v
 
print( my_dict )


#%    SORTED_DCT
my_list = [9, 0, 5]
print( sorted(my_list) )

my_dict = {"a":9, "b":0, "c":5}

def sorted_dct(dct):
      lst = list(dct.items())
      sorted_lst = sorted(lst, key = (lambda t: t[1]) )
      result = dict(sorted_lst)
      return result 

print( sorted_dct(my_dict) )
