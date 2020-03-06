import json


##Clones Beginning##
def Clones(boi):
  x = json.loads(boi)
  for i in range (len(x)):
    print(x[i]['Strength'])
def Clonesmeepmoop(boi):
	x = json.loads(boi)
	for i in range(len(x)):
	########Strength###################
		print("_______________________")
		print(x[i]['Name'])
		if (x[i]['Strength'] >= 90):
			print ("Clones Strength - UH-OH. CLONE STRENGTH TOO HIGH. RESET INITIATED.")
			
			print("_______________________")
		elif (x[i]['Strength'] >= 25):
			print ("Clones Strength - OKAY.")
			print("_______________________")
		else:
			print("Clones Strength - UH-OH. CLONE STRENGTH TOO LOW. RESET INITIATED")
			print("_______________________")

		#########Intellect################
		if (x[i]['Intelligence'] >= 90):
			print ("Clones Intellect - UH-OH. CLONE INTELLECT TOO HIGH. RESET INITIATED")
			print("_______________________")
		elif (x[i]['Intelligence'] >= 25):
			print ("Clones Intellect - OKAY.")
			print("_______________________")
		else:
			print("Clones Intellect - UH-OH. CLONE INTELLECT TOO LOW. RESET INITIATED")
			print("_______________________")

		#########Charisma##################
		if (x[i]['Charisma'] >= 90):
			print ("Clones Charisma - UH-OH. CLONE CHARISMA TOO HIGH. RESET INITIATED")
			print("_______________________")
		elif (x[i]['Charisma'] >= 25):
			print ("Clones Charisma - OKAY.")
			print("_______________________")
		else:
			print("Clones Charisma - UH-OH. CLONE CHARISMA TOO LOW. RESET INITIATED")
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
  if (Education < 2):
    print("NOT SMART ENOUGH. GO BACK TO SCHOOL.")
    #del bigbrain
  else:
    print("CLONE OKAY.")
##Education End##
#Continuity()
#Climate()
#Education()
