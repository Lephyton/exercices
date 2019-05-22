def get_vowels_numbers(word):
    nbr_vowels = 0
    for letter in word :
        if letter in ["a" ,"e", "i" ,"o","y" ,"u"] :
            nbr_vowels += 1
    return nbr_vowels

word = input("entrer un mot :")
print ( word, "à : ", get_vowels_numbers(word))

