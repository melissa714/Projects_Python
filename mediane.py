#Median 

list1=[12,18,16,20,2,8,25,23,25]
# la methode sort permet de trier la liste du plus petit au plus grand(decroissant)
list1.sort()
# print(list1)
# m2 = list1[len(list1)//2-1]

# m1 = list1[len(list1)//2]
# print(m2)

if len(list1)% 2 == 0:
    m1=list1[len(list1)//2]
    m2 = list1[len(list1)//2-1]
    median=(m1+m2)/2 
else:
    median=list1[len(list1)//2]
print(median)