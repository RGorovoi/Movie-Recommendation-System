# Merging the TMDB 5000 Movie Dataset (tmdb_5000_movies.csv) and TMDB 5000 Credits Dataset (tmdb_5000_credits.csv)
# Parsing and flattening JSON columns (genres, keywords, cast, crew)
# Handling missing values, data type conversions, and duplicates

import pandas as pd
import numpy as np

movies_df = pd.read_csv('Data/tmdb_5000_movies.csv')
credits_df = pd.read_csv('Data/tmdb_5000_credits.csv')

merged_df = pd.merge(movies_df, credits_df, left_on='id', right_on='movie_id', how='inner')
merged_df.drop('movie_id', axis=1, inplace=True)

output_filename = 'Notebooks/tmdb_5000_merged.csv'
merged_df.to_csv(output_filename, index=False)