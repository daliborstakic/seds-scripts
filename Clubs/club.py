import pandas as pn

club_filename = 'clubs.csv'
data_frame_clubs = pn.read_csv(club_filename)

data_frame_clubs = data_frame_clubs[['club_id', 'name', 'domestic_competition_id']]
data_frame_clubs = data_frame_clubs.rename(columns={'domestic_competition_id': 'competition_id'})

competition_filename = '../Competitions/competitions.csv'
data_frame_competitions = pn.read_csv(competition_filename)

merge_df = data_frame_clubs.merge(data_frame_competitions, on='competition_id', how='left')
merge_df = merge_df.rename(columns={'name_x': 'name'}).dropna()
merge_df = merge_df[['club_id', 'name', 'country_id']].dropna()
merge_df = merge_df.convert_dtypes()

merge_df.to_csv('new_clubs.csv', index=False);
