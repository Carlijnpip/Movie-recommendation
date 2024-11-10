# Loading in the datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
df = Title, year, category, runtime, genre = pd.read_excel(r"C:\Users\Carli\Downloads\Movies\movies.xlsx")
# Loading the dataset, for this I used the IMDB top 100 list.
# Getting the input of the user
preferred_genre = input("Enter your preferred genre, choose between Crime, Drama, Thriller, Action, Adventure, Fantasy, Horror, Romance, War, Sci-Fi, Comedy, Music, Animation, Mystery, Biography, Musical, Film-Noir: ")
preferred_era = input("Enter your preferred era: ")
preferred_length = input("Enter your preferred length: ") 
# Sorting the release_year and run_time genre into eras 
def classify_era(year):
    if year >= 1920 and year < 1930:
        return '1920s'
    elif year >= 1930 and year < 1940:
        return '1930s'
    elif year >= 1940 and year < 1950:
        return '1940s'
    elif year >= 1950 and year < 1960:
        return '1950s'
    elif year >= 1960 and year < 1970:
        return '1960s'
    elif year >= 1970 and year < 1980:
        return '1970s'
    elif year >= 1980 and year < 1990:
        return '1980s'
    elif year >= 1990 and year < 2000:
        return '1990s'
    elif year >= 2000 and year < 2010:
        return '2000s'
    elif year >= 2010 and year < 2020:
        return '2010s'
    elif year >= 2020 and year < 2030:
        return '2020s'
    else:
        return 'Unknown Era'

# Creating a new column 'era' in the DataFrame using the classify_era function
df['era'] = df[year].apply(classify_era)

def classify_length(runtime):
    if runtime < 90:
        return 'Short'
    elif 90 <= runtime <= 150:
        return 'Medium'
    elif runtime > 150:
        return 'Long'
    else:
        return 'Unknown Length'

# Create a new column 'length_category' in the DataFrame using the classify_length function
df['length_category'] = df[runtime].apply(classify_length)

# Filtering the movies based on the users input
filtered_movies = df[
    (df[genre].str.contains(preferred_genre, na=False)) & 
    (df['era'].str.contains(preferred_era, na=False) if preferred_era else True) &
    (df['length_category'].str.contains(preferred_length) if preferred_length else True)
]
# Presenting a table containing the recommended movies
if not filtered_movies.empty:
    print("Movies matching your preferences:")
    print(tabulate(filtered_movies[[Title, genre, year, runtime ]], headers='keys', tablefmt='pretty', showindex=False))
else: 
    print('Unfortunately, there are no movies matching your preferences')


# I am checking whether the runtimes and years of release of the movies are divided into lengths and eras correctly. 
def test_classify_length():
    runtime = 100
    result = classify_length(runtime)
    assert result == 'Medium' #a movie with a runtime of 100 minutes should give a medium length
def test_classify_era():
    year = 1996
    result = classify_era(year)
    assert result == '1990s' #a movie with the release year 1996 should give the era 1990s.

test_classify_length()
test_classify_era()