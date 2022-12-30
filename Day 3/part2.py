import os

def get_number():
  os.system("clear")
  file = open("rucksack.txt", "r")
  fileText = file.read()
  file.close()
  rucksack = fileText.split("\n") 
  compartment = [rucksack[i:i+3] for i in range(0,len(rucksack),3)]
  alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  beta = []
  print(compartment)
  for n in compartment:
    a = n[0]
    b = n[1]
    c = n[2]
    for z in n:
      for y in z:
        if y in a and y in b and y in c:
          ind = alpha.index(y)+1
          beta.append(ind)
          break
      break
  print(sum(beta))
 
get_number()
