# Computation.py - This program calculates sum, difference, and product of two values.
# Input:  Interactive.
# Output:  Sum, difference, and product of two values.

def main():

    value1String = input("Enter first numeric value: ")
    value1 = float(value1String)
    value2String = input("Enter second numeric value: ")
    value2 = float(value2String)


    # Call calculateSum() here
    print("Sum  is: ", calculateSum(value1, value2))
    # Call calculateDifference() here
    print("Difference  is: ", calculateDifference(value1, value2))
    # Call calculateProduct() here
    print("Product  is: ", calculateProduct(value1, value2))
# End of main() function.

# Write calculateSum() function here.
def calculateSum(x, y):
    a= x + y
    return a

# Write calculateDifference() function here.
def calculateDifference(x, y):
    a= x - y
    return a

# Write calculateProduct() function here.
def calculateProduct(x, y):
    a= x * y
    return a

if __name__ == '__main__':
# Call the main function to run program
    main()
