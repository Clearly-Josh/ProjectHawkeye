#Clone Order: strength, intellect, charisma, low-strength, low-intellect, low-charisma, disabilities! 

Clones = [__, __, __, __, __, __, __]


#Food Order: healthy, unhealthy, poisonous!
Food = [__, __, __]

#water
low_clean = 10

#air
low_clean = 20
atomsphere_stability = 30

clone_intelligence = 95

if ((clone_intelligence > intelligence) or (low_intelligence > clone_intelligence)):
  print("Stinky")