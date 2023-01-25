import datetime


# Cette fonction calcule l'âge d'une personne à 
# partir de sa date de naissance. Elle prend en paramètres
#  l'année (y), le mois (m) et le jour (d) de naissance et 
# renvoie l'âge en années.



def ageCalculator(y,m,d):
    today = datetime.datetime.now().date()
    print(today)
    dob = datetime.date(y,m,d)
    print(dob)
    age=int((today-dob).days / 365.25)
    print(int((today-dob).days))
    print(age)


ageCalculator(1996,12,7)