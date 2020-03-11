 #chips have to be inserted during the cloning portion of this project
#Code needs connect with a number (the number tells us which clone/chip information is going into)
#5% of clones will be 1's, 15% will be 2's, 60% are 3's, 15% will be 4's, and 5% will be 5's
def education(cloneName):
  #name=input("What is the clone's name? ")

  import random

  numberList = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]

  print("The Clone named", cloneName, "will have level", random.choice(numberList), "intelligence. ")

  return(random.choice(numberList))