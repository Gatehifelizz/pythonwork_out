# import random
# print("Random integer between 0 and 9")
# for i in range(4,15):
#   y=random.randrange(5,25)
#  print(y)

import random
import math

# Take inputs
lower = int(input("Enter lower bound:-"))
# Taking inputs
upper = int(input("Enter upper bound:-"))
# generating random number between the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only",
      round(math.log(upper - lower + 1, 2)),
      "chances to get the integer!\n")

# initializing the number of guesses
count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    # taking guessing number as input
    guess = int(input("Guess a number:-"))
    # condition testing
    if x == guess:
        print("Congratulations you did it in", count, "try")
        # once guessed, loop will break
        break
    elif x > guess:
        print("you guessed too small!")
    elif x < guess:
        print("you guessed too high!")
# if guessing is more than required guesses,
# show this output
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\nBetter luck next time")
