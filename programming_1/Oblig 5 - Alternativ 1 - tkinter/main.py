import tkinter as tk
from tkinter import ttk
import movie_module as mm

movie_list = []

window = tk.Tk()
window.title("Bharati's awesome movie list program")
window.geometry("600x400")
window.config(bg="#7f9454")

add_movie_name_label = ttk.Label(text="Movie name:")
add_movie_name_label.grid(row=0, column=0, padx=(20, 0), pady=(10, 10), sticky="w")
add_movie_name_entry = ttk.Entry()
add_movie_name_entry.grid(row=0, column=1, padx=(20, 0), pady=(10, 10), sticky="w")

add_release_year_label = ttk.Label(text="Release year:")
add_release_year_label.grid(row=1, column=0, padx=(20, 0), pady=(0, 10), sticky="w")
add_release_year_entry = ttk.Entry()
add_release_year_entry.grid(row=1, column=1, padx=(20, 0), pady=(0, 10), sticky="w")

add_rating_label = ttk.Label(text="Rating:")
add_rating_label.grid(row=2, column=0, padx=(20, 0), pady=(0, 10), sticky="w")
add_rating_entry = ttk.Entry()
add_rating_entry.grid(row=2, column=1, padx=(20, 0), pady=(0, 10), sticky="w")

add_description_label = ttk.Label(text="Description:")
add_description_label.grid(row=3, column=0, padx=(20, 0), pady=(0, 10), sticky="w")
add_description_entry = ttk.Entry()
add_description_entry.grid(row=3, column=1, padx=(20, 0), pady=(0, 10), sticky="w")

add_movie_button = ttk.Button(text="Add movie", command=lambda: mm.addMovie(movie_frame, movie_list, add_movie_name_entry, add_release_year_entry, add_rating_entry, add_description_entry))
add_movie_button.grid(row=4, column=0)

delete_movie_name_entry = ttk.Entry()
delete_movie_name_entry.grid(row=5, column=0, padx=(20, 0), pady=(10, 10), sticky="w")
delete_movie_button = ttk.Button(text="Delete movie", command=lambda: mm.deleteMovie(movie_frame, movie_list, delete_movie_name_entry))
delete_movie_button.grid(row=5, column=1)

movie_frame = ttk.LabelFrame(window, text='Movies')
movie_frame.grid(row=0, column=2, rowspan=10, sticky="w", padx=(20, 0))

window.mainloop()