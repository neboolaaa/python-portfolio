from intro import intro
import time
intro

time.sleep(.2)
choice = input("You enter the first room and see two Versace tailored suits sitting on the table. Do you choose to wear the blue or the black suit?\n").lower()

if choice == "black":
  time.sleep(.2)
  print("You suit up, looking dapper as always, and progress to the next room...")
  time.sleep(.5)
  drink = input("The next room has a bar. You approach and the bartender asks you care for a drink? Y or N?\n").lower()
  if drink == "y":
    time.sleep(.2)
    print("Of course you do! You're an MI6 agent! You down 'The Vesper', made from “three measures of Gordon's, one of vodka, and half a measure of Kina Lillet, before walking through the door at the back wall...")
    time.sleep(.5)
    transport = input("You find yourself in a garage with 3 options to get to a Serbian missile site, buried in the side of a mountain, and stop Blofeld in his tracks! Do you choose a car, plane or submarine?\n").lower()
    if transport == "car":
      time.sleep(.2)
      print("You grab the keys to your '64 DB5 and speed off. Little do you remember you had a couple of Vespers back at the base! You spin out of control and sack the Aston. Q will not be pleased...")
      time.sleep(.2)
      print("GAME OVER")
    elif transport == "plane":
      time.sleep(.5)
      print("You jump into the worlds only working Concord jet and the pilot iniates hyperwarp to Serbia. You jump out, deploy your parachute and land on Blowfeld's base, right next to the self-destruct button. How convenient! You press the button and run heroically to safety, saving the world!")
      time.sleep(.2)
      print("YOU WIN!")
    else:
      time.sleep(.2)
      print("Did you not pay attention? The missile site is in a mountain and last time I checked, submarines can't fly or traverse mountainsides! A Double-O agent is always meticulous and wouldn't have ingored such a crucial piece of information! Back to the drawing board...")
      time.sleep(.2)
      print("GAME OVER")
  else:
    time.sleep(.2)
    print("No MI6 agent would ever pass up the opportunity for a drink! You are disqualified! Return to your quarters at once!")
    time.sleep(.2)
    print("GAME OVER")
else:
  time.sleep(.2)
  print("An MI6 agent would never don a blue suit! Remember your training agent...")
  time.sleep(.2)
  print("GAME OVER!")
  