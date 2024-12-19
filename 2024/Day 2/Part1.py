list = open("Python\list.txt", "r")
major = []
for x in list:
    major.append(x.split())

levels = []
for x in major:
    level = []
    for i in x:
        level.append(int(i))
    levels.append(level)

print(levels)

safe = 0 

for x in levels:
    temp = 0
    for i in range(1, len(x)):
        if 1 <= x[i]-x[i-1] <= 3: 
            temp += 1

        elif -3 <= x[i]-x[i-1] <= -1: 
            temp += -1
            
    if abs(temp) == len(x)-1:
        safe += 1
    
print(safe)
