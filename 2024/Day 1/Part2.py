list = open("Python\list.txt", "r")
major = []
for x in list:
    major.append(x.split())

left = []
right = []

for i in major:
    left.append(i[0])
    right.append(i[1])

sim = 0
for i in left:
    count = 0
    for x in right:
        if x == i:
            count += 1
    sim += int(i) * count
print(sim)
