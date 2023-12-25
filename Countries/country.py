import pandas as pd

filename = 'countries_dataset.csv'
data_frame = pd.read_csv(filename)

data_frame['id'] = range(1, len(data_frame) + 1)
data_frame = data_frame[['id', 'name']]

output_filename = 'countries.csv'
data_frame.to_csv(output_filename, index=False)

print(f'DataFrame has been written to {output_filename}')
