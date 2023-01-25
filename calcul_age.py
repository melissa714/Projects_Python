from datetime import datetime


date=datetime.now()
annee=date.year
naissance=int(input("Entrez votre année de naissance svp:"))
calcul_age=(annee-naissance)
print(f" Votre age est {annee} est {calcul_age} ans")

