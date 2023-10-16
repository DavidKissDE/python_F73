
#%
def tree_section(tip_width=1, total_width=10):
      for i in range(0,6,2):
            s = "*" * (tip_width+i)
            print( ("*" * (tip_width+i)).center(total_width) )

def tree(height=3):
      total_width = height*2//1
      n_sections = height//3
      for tip_width in range(1, n_sections*2 ,2):
            tree_section(tip_width, total_width)
      print("###".center(total_width))

print(tree(int(input("Höhe = "))))
