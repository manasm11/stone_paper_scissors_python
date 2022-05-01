import random
STONE = 1
PAPER = 2
SCISSORS = 3

def compWin():
  global compScore
  print("Comp wins")
  compScore += 1

def userWin():
  global userScore
  print("User wins")
  userScore += 1

choices = {
  1: {
    "name": "Stone",
    "func": lambda compChoice: compWin() if compChoice == PAPER else userWin(),
  },
  2: {
    "name": "Paper",
    "func": lambda compChoice: compWin() if compChoice == SCISSORS else userWin(),
  },
  3: {
    "name": "Scissors",
    "func": lambda compChoice: compWin() if compChoice == STONE else userWin(),
  }
}

userScore = 0
compScore = 0

while userScore + compScore < 5:
  userChoice = int(input("Enter your choice (1: Stone, 2: Paper, 3: Scissors) : "))
  compChoice = random.randint(1, 3)
  print(f"User's Choice: {choices[userChoice]['name']}")
  print(f"Comp's Choice: {choices[compChoice]['name']}")
  if userChoice == compChoice:
    print("Draw")
    continue
  choices[userChoice]['func'](compChoice)

print(f"User Score: {userScore}")
print(f"Comp Score: {compScore}")

if userScore > compScore:
  print("YOU WON !!!")
elif userScore < compScore:
  print("COMP WON !!!")
else:
  print("ITS DRAW !!!")