import pandas as pd

# Main csv file
main_csv_path = 'competitions.csv'
main_df = pd.read_csv(main_csv_path)

# Only wanted values for field "country_name'
wanted_countries = ['England', 'Spain', 'Germany', 'Italy', 'France']

# Removing unwanted values
main_df = main_df[(main_df['country_name'].isin(wanted_countries)) & (main_df['type'] == 'domestic_league')]

# Selecting only wanted fields
main_df = main_df[['competition_id', 'name', 'type', 'country_id', 'country_name']]

print(main_df)

# Csv file to which we map country names
mapping_csv_path = 'countries.csv'
mapping_df = pd.read_csv(mapping_csv_path)

# We merge them by country name
merged_df = pd.merge(main_df, mapping_df, on='country_name', how='left')

# Set new country_id from the other csv file
merged_df['country_id'] = merged_df['country_id_y']

# Remove the unnecessary id field
merged_df = merged_df.drop(columns=['country_id_y'])

# Only select wanted fields
merged_df = merged_df[['competition_id', 'name', 'type', 'country_id']]

merged_df.to_csv('new_competitions.csv', index=False)
