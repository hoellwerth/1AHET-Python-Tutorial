from random import randint

def rollDice(n):
  numbers = []
  for _ in range(n):
    numbers.append(randint(1, 6))
  
  return numbers

def getInput():
  return int(input("Wie oft möchten Sie würfeln? "))

def countSix():
  times = 0

  for i in rollDice(getInput()):
    if i == 6:
      times += 1
  
  return times

print(f"Die Nummer 6 kam {countSix()} Mal vor!")