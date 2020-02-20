#Clone Order: strength, intellect, charisma, low-strength, low-intellect, low-charisma, disabilities, 
Clones = [100,25,85,20,75,30,100,10,2]

#food
healthy = 50
unhealthy = 20
poisonous = 0

#water
low_clean = 10

#air
low_clean = 20
atomsphere_stability = 30

clone_intelligence = 95

if ((clone_intelligence > intelligence) or (low_intelligence > clone_intelligence)):
  print("Stinky")