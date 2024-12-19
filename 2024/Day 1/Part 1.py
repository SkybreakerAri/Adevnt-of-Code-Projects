list = open("Python\list.txt", "r")
major = []
for x in list:
    major.append(x.split())

loc1 = []
loc2 = []
for x in major:
    loc1.append(int(x[0]))
    loc2.append(int(x[1]))
loc1.sort()
loc2.sort()

dist = []

for i in range(len(loc1)):
    diff = abs(loc2[i]-loc1[i])
    dist.append(diff)

ans = sum(dist)
print(ans)
