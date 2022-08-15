# Creating and empty packing list
program_open = True
packing_list = []
# print out the commands for the user
print("What do you want to do? These are your options:")
print("1. Add something to the packing list.")
print("2. Delete something in the packing list.")
print("3. Change an item in the packing list.")
print("3. Print out the packing list.")
print("4. Exit the program.")

# using while loop and include the int(intiger) and input.
while program_open:
    command = int(input("What do you want to do? Enter a number: "))

    if command == 1:    # adding an item to the packing list
        item_to_add = input("What do you want to add? ")
        packing_list.append(item_to_add)
        print(f"You added {item_to_add} to the list.")
    elif command == 2:   # deleting an item to the packing list
        item_to_delete = input("What do you want to delete? ")
        packing_list.remove(item_to_delete)
        print(f"You remove {item_to_delete} to the list.")
    elif command == 3:    # changing an item to the packing list
        item_to_change = input("What item do you want to change? ")
        item_to_change_to = input("What do you want to change the item to? ")
        packing_list[packing_list.index(item_to_change)] = item_to_change_to
        print(f"You changed {item_to_change} to {item_to_change_to} in the list.")
    elif command == 4:     # printing out the packing list
        print("Here is the packing list:")
        for item in packing_list:
            print(item)
    elif command == 5:    # exiting the programme by breaking the while loop
        print("You are now exiting the program...")
        program_open = False
    else:
        print("That is not an option.")