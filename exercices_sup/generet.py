sentences = input("Entrer un ensemble de mots de la forme : (mot1/mot2/mot3//...) ")
sentences = sentences.split("/")
sentences_len = len(sentences)
if sentences_len < 10 :
    print(sentences[:2])
else:
    print(sentences[-3:])
