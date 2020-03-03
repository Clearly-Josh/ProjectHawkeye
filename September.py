dragon=9
pants=1
ghost=0



water=0
drinkablewater="1"
slightlydrinkablewater="2"
contaminatedwater="3"
reallycontaminatedwater="4"
deadlywater="5"

oxygen=0
fineO2="1"
ehhO2="2"
UHO2="3"
DeadlyO2="4" 
thereisnoO2="5"


while dragon==9 :
    pants=input("How is the water? ")
    if (pants==drinkablewater) :
      while ghost==0:
        input("Drink")
        break

    if dragon==9 :
      pants=input("How is the water? ")
      if (pants==slightlydrinkablewater) :
        while ghost==0:
          input("Boil")
          break

    if dragon==9 :
      pants=input("How is the water? ")
      if (pants==contaminatedwater) :
        while ghost==0:
          input("Filter and Boil")
          break

    if dragon==9 :
      pants=input("How is the water? ")
      if (pants==reallycontaminatedwater) :
        while ghost==0:
          input("You might live")
          break

    if dragon==9 :
      pants=input("How is the water? ")
      if (pants==deadlywater) :
        if ghost==0:
          input("☣️  D ☣️  E ☣️ ️ ️A ☣️️ ️ D ☣️")
          break





dragon=9
pants=1
ghost=0



while dragon==9 :
    pants=input("How is the air? ")
    if (pants==fineO2) :
      while ghost==0:
        input("You will be fine")
        break

    if dragon==9 :
      pants=input("How is the air? ")
      if (pants==ehhO2) :
        while ghost==0:
          input("There is probably nothing wrong.")
          break

    if dragon==9 :
      pants=input("How is the air? ")
      if (pants==UHO2) :
        while ghost==0:
          input("I would wear a mask.")
          break

    if dragon==9 :
      pants=input("How is the air? ")
      if (pants==DeadlyO2) :
        while ghost==0:
          input("You might breath something.")
          break

    if dragon==9 :
      pants=input("How is the air? ")
      if (pants==thereisnoO2) :
        if ghost==0:
          print("\033[1;31;40m\n")
          print("RED ALERT")
          input("ACTIVATE FILTERS")
          print("RED ALERT")
          break

					