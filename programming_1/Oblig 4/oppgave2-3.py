##oppgave2.A#

#created å class name and define the film name, releaseyear and rating.

class Film:
    def __init__(self, name, releaseyear, rating):
        self.name = name
        self.releaseyear = releaseyear
        self.rating = rating

    def print_movie(self):
        print(f"{self.name} was released in {self.releaseyear} and currently has a score of {self.rating}")


#devided the movie by movie1, movie2 and movie3.
movie1 = Film("Inception", 2010, 8.8)
movie2 = Film("The Martian", 2015, 8.0)
movie3 = Film("Joker", 2019, 8.4)



#print the value of function.
print(f"{movie1.name} was released in {movie1.releaseyear} and currently has a score of {movie1.rating}")
print(f"{movie2.name} was released in {movie2.releaseyear} and currently has a score of {movie2.rating}")
print(f"{movie3.name} was released in {movie3.releaseyear} and currently has a score of {movie3.rating}")


##oppgav2.B#

#printing all the information from about the movie objects created in the previous subtask.
print("\n")
movie1.print_movie()
movie2.print_movie()
movie3.print_movie()