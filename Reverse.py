# Reverse.py - This program reverses numbers stored in an list.
# Input:  Interactive.
# Output:  Original contents of list and the reversed contents of the list.
result = []

def main():

    numbers = [9, 8, 7, 6, 5]

    # Print contents of list
    print("Original contents of list:")
    for item in numbers:
        print(item)
    # Call reverselist function here
    result = reverseList(numbers)
    # Print contents of reversed list
    print("Reversed contents of list:")
    for item in result:
        print(item)
# End of main() function.


# Write reverselist function here.
def reverseList(array):
    reverse = []
    for i in range(len(array),0,-1):
        reverse.append(array[i-1])
    return reverse

# End of Reverse class.

if __name__ == '__main__':
# Call the main function to run program
    main()
