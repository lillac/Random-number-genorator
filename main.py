print("Random number generator")
from random import randrange 
a = randrange(0, 10)
b = randrange(0, 20)
c = randrange(0, 30)
d = randrange(0, 40)
e = randrange(0, 50)
f = randrange(0, 60)
g = randrange(0, 70)
h = randrange(0, 80)
i = randrange(0, 90)
j = randrange(0, 100)
print("To generate a random number, between x and y:")
ask = input("Enter a for 0-10, b for 0-20, c for 0-30, d for 0-40 and so on. Highest is j (0-100)")
if ask == "a":
  print(a)
elif ask == "b":
  print(b)
elif ask == "c":
  print(c)
elif ask == "d":
  print(d)
elif ask == "e":
  print(e)
elif ask == "f":
  print(f)
elif ask == "g":
  print(g)
elif ask == "h":
  print(h)
elif ask == "i":
  print(i)
elif ask == "j":
  print(j)
else:
  print("Must be between a-j")











