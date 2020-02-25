
#Arrays
Clones = []
#######

#Choosing Number Of Elements!
print("------------------------------------------")
print("Enter your Clones stats in order of:")
print("------------------------------------------")
print("strength, intellect, charisma")
print("------------------------------------------")

n = int(input("Enter number of elements : ")) 
print("------------------------------------------")

# @GeeksForGeeks
#Adding Numbers!
for i in range(0, n): 
  ele = int(input())
  Clones.append(ele)
print(Clones)

if (Clones[0] >= 90):
  print ("Clones Strength - Uh-Oh")
elif (Clones[0] >= 25):
  print ("Clones Strength - Yes")
else:
  print("Clones Strength - Uh Oh")

if (Clones[1] >= 90):
  print ("Clones Intellect - Uh Oh")
elif (Clones[1] >= 25):
  print ("Clones Intellect - Yes")
else:
  print("Clones Intellect - Uh-Oh")

if (Clones[2] >= 90):
  print ("Clones Charisma - Uh-Oh")
elif (Clones[2] >= 25):
  print ("Clones Charisma - Yes")
else:
  print("Clones Charisma - Uh-Oh")