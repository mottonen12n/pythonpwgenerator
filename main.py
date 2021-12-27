import random as r

words = ["toys", "toothpaste", "hope", "pump", "quicksand", "transport", "skirt", "thunder", "profit", "decision", "eyes", "birth", "trouble", "idea", "rate", "reward", "toy", "arm", "plane", "respect", "crime", "word", "wood", "apparatus", "tree", "judge", "tin", "oatmeal", "trail", "visitor", "key", "bead", "scene", "teeth", "force", "self", "tray", "snow", "driving", "flame", "underwear", "crow", "school", "throat", "existence", "laugh", "rock", "tail", "nation", "air"]



def mainMenu():
  loop = True
  try:
    while(loop):
      print("Make a selection:\n")
      selection = input("1: Generate Password\n2: Change Password Schema")
      if selection == "1":
        print("1")
      elif selection == "2":
        print("2")
      elif selection == "0":
        loop = False

  except(Exception): 
    print("error")

def getLowerWord():
  return r.choice(words)

def getUpperWord():
  return str.upper(r.choice(words))

def generatePW():


mainMenu()

