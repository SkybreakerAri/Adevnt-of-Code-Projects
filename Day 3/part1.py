import os

def get_unique():
  os.system("clear")
  file = open("rucksack.txt", "r")
  fileText = file.read()
  file.close()
  rucksack = fileText.split("\n")
  compartment = []
  alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  beta = []
  for x in rucksack:
    a = x[0:(int(len(x)/2))]
    b = x[(int(len(x)/2)):(int(len(x)))]
    sep = [a] + [b]
    compartment.append(sep)
    for n in a:
      if n in b:
        ind = alpha.index(n)+1
        beta.append(ind)
        break

  print(sum(beta))

  
get_unique()
