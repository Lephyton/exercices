num_real = 122
while num_real in range(1, 1000):
    number = int((input("Entrer un nobre")) )
    if number == num_real:
        print("c'est bon et fin du jeux")
    elif number < num_real :
        print("c'est trop petit")
    elif number > num_real:
        print("c'est trop grand")