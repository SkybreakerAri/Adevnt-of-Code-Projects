def get_numbers():
  os.system("clear")
  file = open("elf.txt","r")
  fileText = file.read()
  file.close()
  elf = fileText.split("\n\n")
  calories = [item.split("\n") for item in elf]
  del calories[239]
  elven_food = []
  for i in calories:
    smth1 = []
    for x in i:
      smth1.append(x)
    smth = []
    for x in smth1:
      num = int(x)
      smth.append(num)
    food = sum(smth)
    elven_food.append(food)
  print(elven_food)
  total = []
  
 get_numbers()
