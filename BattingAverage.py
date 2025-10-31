# Initialize an integer for list size here.
maxAverages = 8

# Initialize list here.
averages = []

# Write a loop to get batting averages from user and add to list.
for i in range(maxAverages):
    # String version of batting average input by user.
    averageString = input("Enter a batting average: ")
    # Use this variable to store the batting average input by user.
    battingAverage = float(averageString)
    # add value to list.
    averages.append(battingAverage)

# Use these variables to store the minimim and maximum batting averages.
# Assign the first element in the list to be the minimum and the maximum.
min = averages[0]
max = averages[0]

# Start out your total initialized to 0.

total = 0


# Write a loop here to access list values starting with averages[1]
for i in range(maxAverages):
    # Within the loop test for minimum and maximum batting averages.
    if averages[i] < min:
        min = averages[i]

    if averages[i] > max:
        max = averages[i]

    total += averages[i]

# Also accumulate a total of all batting averages.
averages = total / maxAverages

# Calculate the average of the 8 averages.
# Print the averages stored in the averages list.
# Print the maximum batting average, minimum batting average, and average batting average.
print("Minimum batting average is " + str(min))
print("Maximum batting average is " + str(max))
print("Average batting average is " + str(averages))
