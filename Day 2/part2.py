import os

def get_score():
  os.system("clear")
  file = open("guide.txt", "r")
  fileText = file.read()
  file.close()
  pair = fileText.split("\n")
  elf1 = [item.split(' ', 1)[0] for item in pair]
  elf2 = [item.split(' ', 1)[1] for item in pair]
  for i in elf1:
    if i == "A":
      elf1[elf1.index(i)] = 1
    elif i == "B":
      elf1[elf1.index(i)] = 2
    elif i == "C":
      elf1[elf1.index(i)] = 3
  for i in elf2:
    if i == "X" or i == "X ":
      elf2[elf2.index(i)] = 1
    elif i == "Y" or i == "Y ":
      elf2[elf2.index(i)] = 2
    elif i == "Z" or i == "Z ":
      elf2[elf2.index(i)] = 3
  total = 0
  i = 0
  for x in elf2:    
    if x == 1:
      if elf1[i] == 1:
        total += x + 2
      elif elf1[i] == 2:
        total += x + 0
      else:
        total += x + 1
    elif x == 2:
      total += elf1[i] + 1 + x
    elif x == 3:
      if elf1[i] == 3:
        total += 7
      else: 
        total += elf1[i] + 1 + 2*x
    i +=1

  print(total)
  

get_score()
