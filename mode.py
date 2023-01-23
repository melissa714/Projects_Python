list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

frequence={}
for i in list1:
    frequence.setdefault(i,0)
    frequence[i]+=1


frequent=max(frequence.values())
for i,j in frequence.items():
    if j == frequent:
        mode = i
print(mode)
