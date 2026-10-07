from ast import Name
def Right_triangle(name):

  print("\nRigle angle triangle :")

  for i in range(1, len(name) + 1):

    print(" ".join(name[:i]))


def Left_triangle(name):

  print("\nLeft angle triangle triangle :")

  for i in range(1, len(name) + 1):
     print("  " * (len(name) - i) + " ".join(name[:i]))


  def Pyramid(name):

    print("\nPyramid :")

    for i in range(1, len(name) + 1):

      print(" " * (len(name) - i) * 2 + " ".join(name[:i]))

#  Get name

name = input("Enter your name : ")

# Menu
print("\nChoose a pattern")
print(" 1. Right triangle :")
print(" 2. Left triangle :")
print(" 3. Pyramid :")


choice = input("Enter your choice (1/2/3) :")

if choice == "1":
    Right_triangle(name)

elif choice == "2":
    Left_triangle(name)

elif choice == "3":
    pyramid(name)
else:
    print("Invalid choice! Please press 1, 2, or 3.")

