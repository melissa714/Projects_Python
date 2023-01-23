
import getpass

authen={"melissa":"parfaite","gueu":"78geueP","parfaite":"parfaite","justin":"justin145","kanan":"parfait"}
print(type(authen))

user=str(input("Entrez votre nom d'utilisateur svp:"))

pwd = getpass.getpass("entrez le mot de passe pour l'utilisateur %s : " % user)
print(user, pwd)


if user in authen and authen[user] == pwd:
    print("super vous ètes connecté(e)  avec succes")
else:
    print("désolé les identifiant ne correspondent pas")


