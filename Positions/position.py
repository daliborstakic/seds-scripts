import pandas as pd

# The file from which we generate positions
file_name = 'players.csv'

data_frame = pd.read_csv(file_name)

# Select the position and sub position field and drop duplicates
data_frame = data_frame[['position', 'sub_position']].drop_duplicates()
# Remove missing values
data_frame = data_frame.dropna()

# Reset the index since some rows have been dropped
data_frame.reset_index(drop=True)
# Insert a new field 'position_id' which will generate from 1 to the number of positions
data_frame.insert(loc=0, column='position_id', value=range(1, len(data_frame) + 1))

# Write to new file 'positions.csv'
data_frame.to_csv('positions.csv', index=False)

