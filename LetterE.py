# LetterE.py - This program prints the letter E with 3 asterisks
# across and 5 asterisks down.
# Input:  None.
# Output: Prints the letter E.

num_across = 3  # Number of asterisks to print across.
num_down = 5  # Number of asterisks to print down.

for r in range(num_down): # Write a loop to control the number of rows.
    for c in range(num_across): # Write a loop to control the number of columns
       if (r%2 == 0): # Decide when to print an asterisk in every column.
          print("*", end="")
       elif (c == 0): # Decide when to print asterisk in column 1.
          print("*", end="")
       else: # Decide when to print a space instead of an asterisk.
          print(" ", end="")
    print("\n") # Figure out where to place this statement that prints a newline.
