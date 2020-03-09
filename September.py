# dragon=8
# pants=1
# ghost=0



# water=0
# drinkablewater="1"
# slightlydrinkablewater="2"
# contaminatedwater="3"
# reallycontaminatedwater="4"
# deadlywater="5"





# while dragon==9 :
#     pants=input("How is the water? ")
#     if (pants==drinkablewater) :
      
#         input("Drink")
#         

#       if dragon==9 :
#         pants=input("How is the water? ")
#       if (pants==slightlydrinkablewater) :
        
#           input("Boil")
#           
          
          
#       if dragon==9 :
#         pants=input("How is the water? ")
#       if (pants==contaminatedwater) :
        
#           input("Filter and Boil")
#           
      
#       if dragon==9 :
#         pants=input("How is the water? ")    
#       if (pants==reallycontaminatedwater) :
        
#           input("You might live")
#           
#       if dragon==9 :
#         pants=input("How is the water? ")
#       if (pants==deadlywater) :
#         if ghost==0:
#           input("☣️  D ☣️  E ☣️ ️ ️A ☣️️ ️ D ☣️")
#           
          


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
        

  print("If any numbers are 3 or above, use criminals.")
            