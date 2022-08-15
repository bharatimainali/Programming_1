# created a list of movie where each movie is a dictionary with the data where name, year and rating

# oppgave 5.1
# oppgave A
movies = [
    {
        "name": "Inception",
        "year": 2010,
        "rating": 8.7
    },
    {
        "name": "Inside Out",
        "year": 2015,
        "rating": 8.1
    },
    {
        "name": "Con Air",
        "year": 1997,
        "rating": 6.9
    }
]


# oppgave B
# creating a function where adding a movie in a movie list
# defining the functions with the minimum parameter and adding the movie
def add_movie(list, name, year, rating=5.0):
    list.append({
        "name": name,
        "year": year,
        "rating": rating
    })

# adding the three new movie name
add_movie(movies, "Ray", 2004, 7.7)
add_movie(movies, "umbrella", 1998, 8.2)
add_movie(movies, "Serious", 1995, 7.9)

# oppgave C
# creating the default rating with adding the movie with no rating
add_movie(movies, "Thinker", 2000)


# oppgave 5.2
# oppgave A
# printing out all the film in a list with movies such as it will be seen
def print_movies(movie_list):
    for movie in movie_list:
        print(f"{movie['name']} - {movie['year']} has a rating of {movie['rating']}")


print_movies(movies)


# oppgave B
# creating a function which take a list with movies and calculating the avg rating af all the movies i a list
# and return the avg_rating
def avg_movie_rating(movie_list):
    total_movies = len(movie_list)
    total_sum = 0
    for movie in movie_list:
        total_sum = total_sum + movie["rating"]
    avg_rating = total_sum / total_movies
    return avg_rating

# testing the fuction to print out avg rating
print(f"\nThe average rating is {avg_movie_rating(movies)}")


# oppgave C
# using the function with list of movie and a year number as a parameter and return it
def movies_from_year(movie_list, year):
    new_movie_list = []
    for movie in movie_list:
        if movie["year"] >= year:
            new_movie_list.append(movie)

    return new_movie_list

# printing the movies after the 2010
print_movies(movies_from_year(movies, 2010))


# oppgave 5.3
# oppgave A
# creating the function where a list with movie and filename as parameter, and printing the name of filename of file "movie_titles.txt".
def movie_name_to_file(movie_list, filename):
    file = open(filename, "w")
    movie_titles = ""
    for movie in movie_list:
        movie_titles = movie_titles + f"{movie['name']}\n"
    file.write(movie_titles)
    file.close()


movie_name_to_file(movies, "movie_titles.txt")

# Oppgave B
# making a methode which cqan read the same file which inputparameter to the function.
def print_file_to_console(filename):
    file = open(filename, "r")
    print(f"\n{file.read()}")

# printing out the inholdes
print_file_to_console("movie_titles.txt")




