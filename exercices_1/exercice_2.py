#ouvrir le fichier moock_data le lire 
#recuperer toutes les lignes dont la colone gender est egal à male
#creer  un autre fichier csv et y ecrire ces informations

def read_csv(mon_fichier):
    with open(mon_fichier, 'r') as f:
        lines = f.DictReader()
        for line in lines :
            line = line.split(",")
            print(line)

read_csv("mock_data.csv")
       


 