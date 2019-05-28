import csv




with open('mock_data.csv', 'r') as f:
    csv_read = csv.DictReader(f)
    for row in csv_read:

        with open('contacts_male.csv', 'w') as f2:
            csv_write = csv.writer(f2, delimiter=',')
            for rows in csv_read:
                csv_write.writerow(rows)
       
        
