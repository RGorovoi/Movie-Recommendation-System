import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string

df = pd.read_csv('C:\\Users\\xiyou\\OneDrive\\Desktop\\Data Science Bootcamp 2025\\clean_parsed_tmdb_5000.csv')

#counting the number of movies for each genre category and displaying the top 10
genre_counts = df['genres'].value_counts().head(10)

average_pop_by_genre = df.groupby('genres')['popularity'].mean()
sorted_genre_pop = average_pop_by_genre.sort_values(ascending = False)
top_10_genre_pop = sorted_genre_pop.head(10)
plt.figure(figsize=(10, 4))
top_10_genre_pop.plot(kind='bar', color='blue')
plt.title('Top 10 Movie Genres by Popularity')
plt.xlabel('Genre')
plt.ylabel('Popularity')
plt.grid(axis='y')  #grid created alone y axis
plt.show()


#splits the crew by every name and adds it to the original df and drops the crew column to avoid redundancy
crew_split = df['crew'].str.split(',', expand = True)
merge = df.join(crew_split, how = 'outer')
clean_merge = merge.drop(columns = ['crew'])

#create a new dataframe to hold directors and find the directors of each movie
directors = pd.DataFrame(index = np.arange(len(clean_merge)), columns = np.arange(2))
for i in range(len(clean_merge)):
    for j in range (clean_merge.shape[1]):
        if "(Director)" in str(clean_merge.iloc[i,j]):
            directors.iloc[i,0] = clean_merge.iloc[i,15]
            directors.iloc[i,1] = clean_merge.iloc[i,j]

print(directors.head(5))


df['release_date'] = pd.to_datetime(df['release_date'])
df['year'] = df['release_date'].dt.year
df['10year'] = (df['year']//10)*10
df['genre_split'] = df['genres'].str.split(',')

genre_explode = df.explode('genre_split')
#genre_explode['genre_split'] = genre_explode['genre_split'].str.lstrip()

#graph of most popular genres by count
genre_counts = genre_explode['genre_split'].value_counts().head(10)
print(genre_counts.head(10))
plt.figure(figsize=(7, 6))
genre_counts.plot(kind='bar', color='orange')
plt.title('Top 10 Movie Genres by Frequency')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.grid(axis='y')  #grid created alone y axis
plt.tight_layout()
plt.show()

#graph of top genre of each decade
year_genre_vote = genre_explode.groupby(['10year','genre_split'])['vote_average'].sum()
year_genre_vote = year_genre_vote.reset_index()
year_genre_vote = year_genre_vote.rename(columns = {'vote_average': 'total_vote_average'})
top_decade_index = year_genre_vote.groupby('10year')['total_vote_average'].idxmax()
top_decade_genre = year_genre_vote.loc[top_decade_index]
print (top_decade_genre.head(10))

plt.figure(figsize=(7, 6))
genre_decade = sns.barplot(x = '10year', y = 'total_vote_average', data = top_decade_genre)
labels = top_decade_genre['genre_split']

genre_decade.bar_label(genre_decade.containers[0], labels = top_decade_genre['genre_split'])
plt.title('Top Movie Genre of Each Decade')
plt.xlabel('Decade')
plt.ylabel('Total Vote Average')
plt.grid(axis='y')  #grid created alone y axis
plt.tight_layout()
plt.show()
