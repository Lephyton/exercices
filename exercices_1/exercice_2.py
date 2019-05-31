#ouvrir le fichier moock_data le lire 
#recuperer toutes les lignes dont la colone gender est egal à male
#creer  un autre fichier csv et y ecrire ces informations
 

def read_csv (mon_fichier):
    with open(mon_fichier, 'r') as f:
        lines = f.readlines()
        result = []
        for line in lines :     
            line = line.split("," ) 
            if line[4] == "Male" :
                line = ','.join(line)
                result.append(line) 
                print(line)

        return result
            
def write_csv (mon_fichier, my_list):
     with open(mon_fichier, 'w', encoding = "utf8") as f :
         f.writelines(my_list)


f = read_csv("mock_data.csv")
write_csv("mock_data_male.csv", f) 