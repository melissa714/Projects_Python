s=str(input("entrez le texte svp:"))


unique=set({})
for l in s:
    if l not in unique:
        unique.add(l)
        print(f"le caractere:{l} figure",s.count(l),"dans s")