# replitPython
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
    print("Very smart. You hide out with others who had the same idea as you. You are able to use the products in the store to   survive. Congrats. You lived. Well done.")
  if choice2a =="HOUSE":
    print("2 weeks pass. You run out of food. A zombie breaks in and  you are too weak to fight back. You die.")

