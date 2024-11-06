file = open("instrukcje.txt")
data = []
for f in file:
    f = f.strip()
    f = f.split()
    data.append(f[0])
winner2 = ["?",0]
temp = 0
for i in range(len(data)-1):
    if data[i] == data[i+1]:
        temp += 1
        if temp > winner2[1]:
               winner2 = [data[i],temp]
    else:
        temp = 0
winner2[1] += 1
print(winner2)
    
