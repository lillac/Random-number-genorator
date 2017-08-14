from random import randrange
print('Random Number Generator')
l = int(input('Enter min number'))
h = int(input('Enter max number'))
gu = (randrange(l, h))
st = input("Would you like to try guess the random number? y/n")
if st == 'n':
  print("Okay, here is your random number:")
  print(gu)
elif st == 'y':
  gs = input("Guess..")
  if gs == gu:
    print("Correct!")
  elif gs != gu:
    print("Incorrect..")
    print("The answer is:")
    print(gu)
