def read_csv (mon_fichier, num_lines = 31):
    with open(mon_fichier, 'r') as f:
        lines = f.readlines()

        for line in lines :
            line = line.split("," )
            line =  " {}, est le n° : {}, il s'agit d'un {}, ".format(line[1], line[0], line[4]) 
            print(line)
        return line
            
def write_csv (mon_fichier, my_list):
    with open(mon_fichier, 'w') as f :
         f.writelines(my_list)


f = read_csv("mock_data.csv")
write_csv("mock_data_1.csv", f ) 