age = int (input("Entrer votre âge : "))
if age < 18 :
    prix_total = 7
else :
   prix_total = 12

question = input("souhaitez vous du popcorn ? (N pour non et Y pour oui) ")

if question == "Y":
    prix_total += 5
    print("vous devez payer : ", prix_total, "euros")
else:
    print("merci")