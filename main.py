import random as r

words = ["toys", "toothpaste", "hope", "pump", "quicksand", "transport", "skirt", "thunder", "profit", "decision", "eyes", "birth", "trouble", "idea", "rate", "reward", "toy", "arm", "plane", "respect", "crime", "word", "wood", "apparatus", "tree", "judge", "tin", "oatmeal", "trail", "visitor", "key", "bead", "scene", "teeth", "force", "self", "tray", "snow", "driving", "flame", "underwear", "crow", "school", "throat", "existence", "laugh", "rock", "tail", "nation", "air"]

specials = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+", "="]

numLowers = 1
numUppers = 1
numNums = 2
numSpecials = 1

def main_menu():
  loop = True
  try:
    while(loop):
      print("Make a selection:")
      selection = input("1: Generate Password\n2: Change Password Schema\n0: Exit\n")
      if selection == "1":
        print("Password Generated: ", generate_pw())
      elif selection == "2":
        change_schema()
      elif selection == "0":
        loop = False
      else: print("Invalid input, please try again.")

  except(Exception): 
    print("error")

def get_lower_word():
  return r.choice(words)

def get_upper_word():
  return str.upper(r.choice(words))

def get_number():
  return str(r.randint(0,9))

def get_special():
  return r.choice(specials)

def generate_pw():
  password = ""
  for i in range(numLowers):
    password = password + get_lower_word()
  for i in range(numUppers):
    password = password + get_upper_word()
  for i in range(numNums):
    password = password + get_number()
  for i in range(numSpecials):
    password = password + get_special()
  return password

def change_schema():
  try:
    global numLowers
    numLowers = int(input("Enter number of lowercase words:\n"))
    global numUppers
    numUppers = int(input("Enter number of uppercase words:\n"))
    global numNums
    numNums = int(input("Enter number of numbers:\n"))
    global numSpecials
    numSpecials = int(input("Enter number of special characters:\n"))
  except(Exception): print("Invalid input, please input a number.")
  

main_menu()
#print(get_number())

