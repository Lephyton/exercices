import pandas as pd 

Contact_df = pd.read_csv(mock_data.csv)

Contact_df['format'] = contact_df[['first_name', 'id']].apply(lambda x: f '{x[0]}, est le numero : {x[1]}')




