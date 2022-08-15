# import the randrange from random

from random import randrange

# defining the functions og random, and tryning to printing with design.
def random_number_generator():
    random_number = randrange(0, 100)
    print("*********")
    print(f"** {random_number} ***")
    print("*********\n")

#calling the fuctions many times
random_number_generator()
random_number_generator()
random_number_generator()
