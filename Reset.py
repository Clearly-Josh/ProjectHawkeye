#Arrays
Clones = []
#######

#Choosing Number Of Elements!
print("__________________________________________")
print("Enter your Clones stats in order of:")
print("__________________________________________")
print("strength, intellect, charisma")
print("__________________________________________")

n = int(input("Enter number of elements : ")) 
print("__________________________________________")

# @GeeksForGeeks
#Adding Numbers!
for i in range(0, n): 
  ele = int(input())
  Clones.append(ele)
print("_______________________")

########Strength###################
if (Clones[0] >= 90):
  print ("Clones Strength - Uh-Oh")
  print("_______________________")
elif (Clones[0] >= 25):
  print ("Clones Strength - Yes")
  print("_______________________")
else:
  print("Clones Strength - Uh-Oh")
  print("_______________________")

#########Intellect################
if (Clones[1] >= 90):
  print ("Clones Intellect - Uh-Oh")
  print("_______________________")
elif (Clones[1] >= 25):
  print ("Clones Intellect - Yes")
  print("_______________________")
else:
  print("Clones Intellect - Uh-Oh")
  print("_______________________")

#########Charisma##################
if (Clones[2] >= 90):
  print ("Clones Charisma - Uh-Oh")
  print("_______________________")
elif (Clones[2] >= 25):
  print ("Clones Charisma - Yes")
  print("_______________________")
else:
  print("Clones Charisma - Uh-Oh")  
  print("_______________________")
###########End#####################

