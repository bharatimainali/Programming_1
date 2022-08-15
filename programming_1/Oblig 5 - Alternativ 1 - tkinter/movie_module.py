import tkinter as tk
from tkinter import ttk

class Movie:
    def __init__(self, name, release_year, rating, description):
        self.name = name
        self.release_year = release_year
        self.rating = rating
        self.description = description


def clearFields(fieldArray):
    for field in fieldArray:
        field.delete("0", "end")
        field.insert("0", "")


def clearMovieList(labelframe):
    for item in labelframe.winfo_children():
        item.destroy()

def generateNewLabelFrames(movie_frame, movie_list):
    clearMovieList(movie_frame)
    for index in range(len(movie_list)):
        labelframe = ttk.LabelFrame(movie_frame, text=movie_list[index].name)
        labelframe.grid(row=index, column=2, sticky="w")

        label = ttk.Label(labelframe, text=f"Release Year: {movie_list[index].release_year}\nRating: "
                                           f"{movie_list[index].rating}\nDescription: {movie_list[index].description}")
        label.grid(row=index, column=2, sticky="w")

def addMovie(movie_frame, movie_list, movie_name, release_year, rating, description):
    new_movie = Movie(movie_name.get(), release_year.get(), rating.get(), description.get())
    movie_list.append(new_movie)
    clearMovieList(movie_frame)
    generateNewLabelFrames(movie_frame, movie_list)
    clearFields([movie_name, release_year, rating, description])

def deleteMovie(movie_frame, movie_list, movie_name):
    movie_to_remove = movie_name.get()

    for movie in movie_list:
        if movie.name == movie_to_remove:
            movie_list.pop(movie_list.index(movie))

    clearFields([movie_name])
    clearMovieList(movie_frame)
    generateNewLabelFrames(movie_frame, movie_list)