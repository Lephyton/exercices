def read_contacts ():
     with open(mon_fichier, 'r') as f:
        lines = f.readlines()
     return lines

def write_csv (mon_fichier, my_list):
    with open(mon_fichier, 'w') as f :
         f.writelines(my_list)s


f = read_csv("mock_data.csv")
write_csv("mock_data_1.csv", f )