#%

array1 = [1, 2, 3, 4, 5]
array2 =[4, 5, 6, 7, 8]
# array1 =[1, 2, 3, 4, 5]
# array2= [5, 6, 7, 8]
# array1 = [1, 2, 3, 4, 5]
# array2 = []

def find_common_elements(array1, array2):
      return [x for x in array1 if x in array2]

find_common_elements(array1, array2)