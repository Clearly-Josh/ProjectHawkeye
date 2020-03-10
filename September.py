# dragon=8
# pants=1
# ghost=0


def water(pants):
 
 

    
 dragon=9
 ghost=0 
 water=0
 drinkablewater=1
 slightlydrinkablewater=2
 contaminatedwater=3
 reallycontaminatedwater=4
 deadlywater=5

 x=0

 if dragon==9:
      #pants=input("How is the air? ")
   if (pants==drinkablewater) :
     print("Just drink it.")
      

 if dragon==9 :
    #pants=input("How is the air? ")
   if (pants==slightlydrinkablewater) :
      print("I would filter it but you're good.")
    

 if dragon==9:
    #pants=input("How is the air? ")
   if (pants==contaminatedwater) :
     print("I wouldn't drink until it's filtered. And maybe boiled")
      

 if dragon==9 :
    #pants=input("How is the air? ")
   if (pants==reallycontaminatedwater) :
     print("Don't even think about it.")
      

 if dragon==9 :
    #pants=input("How is the air? ")
    if (pants==deadlywater) :
      print("\033[3;35;40m\n")
      while(x<10):
        print("DEADLY ALERT")
        print("☣☣☣☣☣☣☣")
        print("DEADLY ALERT")
        x+=1
        dragon+=1
        

          


# print("")
# print("")

# dragon=9
# pants=1
# ghost=0


def air(pants):
    
  dragon=9
  ghost=0 
  oxygen=0
  fineO2=1
  ehhO2=2
  UHO2=3
  DeadlyO2=4 
  thereisnoO2=5
  x=0

  if dragon==9 :
      #pants=input("How is the air? ")
    if (pants==fineO2) :
      
      print("You will be fine")
      

  if dragon==9 :
    #pants=input("How is the air? ")
    if (pants==ehhO2) :
      
      print("There is probably nothing wrong.")
      

  if dragon==9 :
    #pants=input("How is the air? ")
    if (pants==UHO2) :
      
      print("I would wear a mask.")
      

  if dragon==9 :
    #pants=input("How is the air? ")
    if (pants==DeadlyO2) :
      
      print("You might breath something.")
      

  if dragon==9 :
    #pants=input("How is the air? ")
    if (pants==thereisnoO2) :
      print("\033[1;31;40m\n")
      while(x<10):
        print("RED ALERT")
        print("ACTIVATE FILTERS")
        print("RED ALERT")
        x+=1
        dragon+=1
        
