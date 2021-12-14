print("Welome human.")

print('It is the year 3000. Welcome to the zombie apocolypse')

choice1 = input('Do you FIGHT or HIDE?')

if choice1 =="FIGHT":
  print("Okay then; prepare for battle.")

  choice1a=input("Choose your weapon: GUN or BAT?")
  if choice1a=="GUN":
    print("You run out of bullets. All you have left are your bare    hands. You are not strong enough. The zombies beat you.    YOU DIE.")

    
  if choice1a=="BAT":
    print("Bam. They are all dead. Not only have you survived, but you have killed all the zombies, saving humanity. Well done,  hero.")

elif choice1 =="HIDE":
  print("Wise choice, *cough* coward *cough*")

  

  choice2a=input("Will you hide in a STORE or HOUSE?")
  if choice2a =="STORE":
    print("You hide out with others. Everyone is stealing products.")
    choice2b=input("Which products do you get? FOOD AND WATER or MEDICAL SUPPLIES?")
    if choice2b=="FOOD AND WATER":
      print("Food and water are essential. Very smart. Others were not as   fortunate as you. There is a starving woman.")
    if choice2b=="MEDICAL SUPPLIES":
      print("A woman has come into the store injured. She is in urgent need of care.")
    choice2c=input("Will you share your rations? YES or NO?")
    if choice2c=="YES":
      print("You have befriened a woman named Katelynn. She shares her      rations with you and you two survive together. After 5 long months, you make it out alive. Congrats.")
    if choice2c=="NO":
      print("You run out of rations. Your time is running out. Your vision  begins to fade as you slowly starve to death. This is the end. You die.")


    
  if choice2a =="HOUSE":
    print("Safe at home, right? But what is that noise? Dozens of zombies are trying to break in.")
    choice2d=input("Do you grab a kitchen KNIFE to stab them? Or hide away in the  BATHROOM, locking the doors.")
    if choice2d=="KNIFE":
      print("There are so many zombies. You are far outnumbed. You put up a strong battle, but it is not enough. The zombies slowly.      sufficate you to death. So tragic.")
    if choice2d=="BATHROOM":
      print("It has been 2 weeks, and you are surviving by drinking tap water and that one bag of expired chex mix you forgot about, as well as those dinner mints you left in there. You slob.")
    choice2e=input("Do you risk GOING OUT for more resources or WAIT it out until  someone comes to rescue you?")
