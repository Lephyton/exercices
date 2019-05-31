
def read_csv (mon_fichier, num_lines = 31):
    with open(mon_fichier, 'r') as f:
        lines = f.readlines()
        lines = lines[:num_lines]
        result = []
        for line in lines :
            line = line.split("," )
            line =  " {}, est le n° : {}, il s'agit d'un {}, ".format(line[1], line[0], line[4]) 
            result.append(line + "\n")
            print(line)
        return result
            
def write_csv (mon_fichier, my_list):
    with open(mon_fichier, 'w', encoding = "utf8") as f :
         f.writelines(my_list)


f = read_csv("mock_data.csv")
write_csv("mock_data_1.csv", f) 