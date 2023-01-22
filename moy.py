# note1=float(input("entrez la moyenne svp:"))
# note2=float(input("Entrez la moyenne svp:"))


# moyenne=(note1+note2)/2

# if moyenne >= 10:
#     print("vous avez la moyenne:",moyenne)
# else:
#     print(f'vous n avez pas la moyenne,la moyenne  est {moyenne}')

liste=int(input("entrez plusieurs note:"))

listes=[x for x in range(liste)]
moyenne=sum(listes)/(len(listes))
print(listes)
print(moyenne)

# for i in range(liste):
#     listes.append(i)
# print(listes)
