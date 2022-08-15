#bruker modulo for å sjekke om tallet er oddetall

print("Odd numbers printed out with a for loop:")
for i in range(9, 101):
    if i % 2 == 1:
        print(i)

# here i use the while loop to count from 9 to 101 and print out only the oddnumber.

print("\nOdd numbers printed out with a while loop:")
current_number = 9
while current_number < 101:
    if current_number % 2 == 1:
        print(current_number)
    current_number = current_number + 1
