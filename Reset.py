##Clones Beginning##
def Clones(boi):
  ########Strength###################
  if (boi[0] >= 90):
    print ("Clones Strength - Uh-Oh")
    print("_______________________")
  elif (boi[0] >= 25):
    print ("Clones Strength - Yes")
    print("_______________________")
  else:
    print("Clones Strength - Uh-Oh")
    print("_______________________")

  #########Intellect################
  if (boi[1] >= 90):
    print ("Clones Intellect - Uh-Oh")
    print("_______________________")
  elif (boi[1] >= 25):
    print ("Clones Intellect - Yes")
    print("_______________________")
  else:
    print("Clones Intellect - Uh-Oh")
    print("_______________________")

  #########Charisma##################
  if (boi[2] >= 90):
    print ("Clones Charisma - Uh-Oh")
    print("_______________________")
  elif (boi[2] >= 25):
    print ("Clones Charisma - Yes")
    print("_______________________")
  else:
    print("Clones Charisma - Uh-Oh")  
    print("_______________________")
##Clones End##

##Continuity Begin##
def Continuity(): #lacapiton
  lacapiton = 50
  Hitler = 98.2
  if (lacapiton > Hitler):
    print("LEADER TOO POWERFUL. RESET INITIATED.")
    del lacapiton
  else:
    print("LEADER SATISFACTORY.")
##Continuity End##


##Climate Beginning##
def Climate():  #globalwarming
  Water = 12
  Oxygen = 2
  if (Water >= 2):
    print("WATER CONTAMINATED, RESET INITIATED.")
    #del globalwarming
  else:
    print("WATER CLEAN, CONTINUE.")
  if (Oxygen >= 2):
    print("OXYGEN CONTAMINATED, RESET INITIATED.")
    #del globalwarming
  else:
    print("OXYGEN CLEAN, CONTINUE.")
##Climate End##

##Education Beginning##
def Education():  #bigbrain
  Education = 1
  if (Education < 2):
    print("NOT SMART ENOUGH. GO BACK TO SCHOOL.")
    #del bigbrain
  else:
    print("CLONE OKAY.")
##Education End##
Continuity()
Climate()
Education()

