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
    if x > elf1[i]:
      if x == 3 and elf1[i] == 1:
        total += x
      else:
        total += 6 + x
    elif x == elf1[i]:
      total += 3 + x
    elif x ==  1 and elf1[i] == 3:
      total += 6 + x
    elif x < elf1[i]:
      if x ==  1 and elf1[i] == 3:
        total += 6 + x
      else:
        total += x
    i +=1

  print(total)
