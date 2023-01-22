import random
n = random.randint(1, 10)
devine = int(input("Entrez le nombre: "))

while n != devine:
    if devine < n:
        print("Trop bas")
        devine = int(input("Entrez le nouveau nombre: "))
    elif devine > n:
        print("Trop haut!")
        devine = int(input("Entrez le nouveau nombre: "))
    else:
      break
print("vous avez bien deviné!!",n)


