import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset directly from a working public source URL
csv_url = "https://raw.githubusercontent.com/slimanesedrati/Investigating-Netflix-Movies/main/data/netflix_data.csv"
netflix_df = pd.read_csv(csv_url)

# Filter the data for movies
netflix_movies_col_subset = netflix_df[netflix_df['type'] == 'Movie']

# Select the columns of interest
netflix_movies_col_subset = netflix_movies_col_subset[['title', 'country', 'genre', 'release_year', 'duration']]

# Initialize a list to store colors based on genre
colors = []

# Assign colors to specific genres to highlight them in the plot
for idx, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == 'Documentaries':
        colors.append('blue')
    elif row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == 'Stand-Up':
        colors.append('green')
    else:
        colors.append('black')

# Set up the visual plot
fig = plt.figure(figsize=(12, 8))

# Create a scatter plot of duration versus release year
plt.scatter(
    netflix_movies_col_subset['release_year'], 
    netflix_movies_col_subset['duration'], 
    c=colors, 
    alpha=0.6
)

# Add titles and labels
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Display the plot
plt.show()
