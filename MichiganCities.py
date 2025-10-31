# MichiganCities.py - This program prints a message for invalid cities in Michigan.
# Input:  Interactive.
# Output:  Error message or nothing.

# Initialized array of cities in Michigan.
citiesInMichigan = ["Acme", "Albion", "Detroit", "Watervliet", "Coloma", "Saginaw", "Richland", "Glenn", "Midland", "Brooklyn"]

# Get user input.
# name of city to look up in array.
inCity = input("Enter name of city: ")

# Write your loop here.
for i in range(len(citiesInMichigan)):
	# Write your test statement here to see if there is a match.
	# Set the flag to true if city is found.
	if citiesInMichigan[i] == inCity:
		foundIt = True
		break
	else:
		foundIt = False

# Test to see if city was not found to determine if
# "Not a city in Michigan." message should be printed.
if foundIt:
	print("City found.")
else:
	print("Not a city in Michigan.")
