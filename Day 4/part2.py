def get_number():
  file1 = open("clean.txt", "r")
  clean = file1.read().splitlines()
  icount = 0
  for line in clean:
    team1, team2 = [list(map(int, pair.split('-'))) for pair in line.split(",")]  
    if team1[0] <= team2[0] and team1[1] >= team2[0]:
      icount += 1

      
    elif team1[0] >= team2[0] and team1[0] <= team2[1]:
      icount += 1


  print("The number of overlapping teams is: " + str(icount))
  

get_number()
