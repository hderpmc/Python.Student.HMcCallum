# ChangeCase.py - This program converts a string to lowercase and uppercase.
# Input:  Interactive
# Output:  Uppercase and lowercase versions of the user-entered string.

def main():
    sample = input("Enter a string or done when you want to quit.")

    while sample != "done":
        # Call lower() function here and print the result.
        result = sample.lower()
        print("Lowercase: " + result)
        # Call upper() function here and print the result.
        result = sample.upper()
        print("Uppercase: " + result)
        sample = input("Enter a string or done when you want to quit.")
# End of main() function.

if __name__ == '__main__':
# Call the main function to run program
    main()
