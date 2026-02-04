# Multiply.py - This program prints the numbers 0 through 10 along
# with these values multiplied by 2 and by 10.
# Input:  None.
# Output: Prints the numbers 0 through 10 along with their values multiplied by 2 and by 10.

head1 = "Number:"
head2 = "Multiplied by 2:"
head3 = "Multiplied by 10:"

# number used to control loop.
MAX_NUM = 10

print("0 through 10 multiplied by 2 and by 10" + "\n")

# Initialize loop control variable.
numberCounter = 0
# Write your counter controlled while loop here
while numberCounter <= 10:
    byTwo = numberCounter * 2 # Multiply by 2
    byTen = numberCounter * 10 # Multiply by 10
    print(head1, numberCounter)
    print(head2, byTwo)
    print(head3, byTen)
    numberCounter += 1 # Next number.
