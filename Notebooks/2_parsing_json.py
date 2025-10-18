# Parsing and flattening JSON columns (genres, keywords, cast, crew)
import pandas as pd
import json

merged_df = pd.read_csv('../Data/clean_tmdb_5000_merged.csv')

# Parse genres column, replace with comma-separated list
def parse_genres(x):
    try:
        genres = json.loads(x)
        return ', '.join([genre['name'] for genre in genres])
    except:
        return ''
merged_df['genres'] = merged_df['genres'].apply(parse_genres)

# Parse keywords column, replace with comma-separated list
def parse_keywords(x):
    try:
        keywords = json.loads(x)
        return ', '.join([keyword['name'] for keyword in keywords])
    except:
        return ''
merged_df['keywords'] = merged_df['keywords'].apply(parse_keywords)

# Parse cast column (top 6 actors), replace with comma-separated list
def parse_cast(x):
    try:
        cast = json.loads(x)
        return ', '.join([actor['name'] for actor in cast[:6]])
    except:
        return ''
merged_df['cast'] = merged_df['cast'].apply(parse_cast)

# Parse crew column (all crew members with their roles), replace with comma-separated list
def parse_crew(x):
    try:
        crew = json.loads(x)
        return ', '.join([f"{member['name']} ({member['job']})" for member in crew])
    except:
        return ''
merged_df['crew'] = merged_df['crew'].apply(parse_crew)

# Parse production companies column, replace with comma-separated list
def parse_production_companies(x):
    try:
        companies = json.loads(x)
        return ', '.join([company['name'] for company in companies])
    except:
        return ''
merged_df['production_companies'] = merged_df['production_companies'].apply(parse_production_companies)

# Parse spoken languages column, replace with comma-separated list
def parse_spoken_languages(x):
    try:
        languages = json.loads(x)
        return ', '.join([language['name'] for language in languages])
    except:
        return ''
merged_df['spoken_languages'] = merged_df['spoken_languages'].apply(parse_spoken_languages)

# Parse production countries column, replace with comma-separated list
def parse_production_countries(x):
    try:
        countries = json.loads(x)
        return ', '.join([country['name'] for country in countries])
    except:
        return ''
merged_df['production_countries'] = merged_df['production_countries'].apply(parse_production_countries)

output_filename = '../Data/clean_parsed_tmdb_5000.csv'
merged_df.to_csv(output_filename, index=False)
print(f"Parsed data saved to {output_filename}")

# Missing values, data type conversions, and duplicate removal were handled during data cleaning