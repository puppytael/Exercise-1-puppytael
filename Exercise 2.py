# Problem 1 Defening some variables
ice_cream_rating = 6
sleeping_rating = 5
print(ice_cream_rating)
print(sleeping_rating)
print()
# Problem 2 Reading in variable values
first_name = input("What is your first name")
last_name = input("What is your last name")
my_name = first_name + last_name
print(my_name)
# Problem 3 bit of math
happiness_rating = (ice_cream_rating + sleeping_rating) / 2
print(happiness_rating)
# Problem 4 data types
print(type(happiness_rating))
print(type(sleeping_rating))
print(type(first_name))
# Problem 5
print("My name is", my_name, "and i give ice cream a rating of", ice_cream_rating, "out of 10 ")
print("My name is", my_name, "and i give ice cream a rating of", sleeping_rating, "out of 10 ")
print("My name is", my_name, "and based on the factors above my hapiness rating is", happiness_rating, "out of 10")
print()
print()
# Exercise 2
# Problem 1 creating lists
station_names = ["lighthouse", "Harmaja", "Suomenlinna aaltopoiju", "Kumpula", "Kaisaniemi"]
station_start_years = [2003, 1989, 2016, 2005, 1844]
print(station_names)
print(station_start_years)
assert (len(station_names)) == 5, 'The station_names list should have 5 items.'
assert (len(station_start_years)) == 5, 'The station_start_years list should have 5 items.'
assert (station_names[0]) == "lighthouse", 'The first item in the station_names list should be "lighthouse"'
assert (station_start_years[0]) == 2003, 'The first item in the station_start_years list should be 2003'
print()
# Modifying lists
station_names.extend(["Malmi airfield", "Vuosaari harbour", "Kaivopuisto"])
print(station_names)
station_start_years.extend([1937, 2012, 1904])
print(station_start_years)
assert len(station_names) == 8, 'The station_names list should have 8 items.'
assert len(station_start_years) == 8, 'The station_start_years list should have 8 items.'
assert station_names[-1] == 'Kaivopuisto', 'The last item in the station_names list should be "Kaivopuisto"'
assert station_start_years[-1] == 1904, 'The last item in the station_start_years list should be 1904'
print()
# sorting lists
# sorting station names alphabetical order
station_names.sort()
print(station_names)
station_start_years.sort()
station_start_years.reverse()
print(station_start_years)
assert station_names[0] == 'Harmaja', 'The first item in the station_names list should be "Harmaja"'
assert station_start_years[0] == 2016, 'The first item in the station_start_years list should be 2016'
print()
# zipping station years single line
x = zip(station_names, station_start_years)
station_start_years.sort(reverse=True)
print(tuple(x))
# Assessing monthly average temperatures
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
average_temp = [-3.5, -4.5, -1.0, 4.0, 10.0, 15.0, 18.0, 16.0, 11.5, 6.0, 2.0, -1.5]
# The following code works on the basis of index value.
# Corresponding elements of two lists are extracted using a common index value.
selected_month_index = input([])
selected_month = int(selected_month_index)
month = str(input(months[selected_month]))  # [0= Jan, ..., 11 = Dec, i.e. 4 = May]
print(month)
temp = str(input(average_temp[selected_month]))  # [0= -3.5, ..., 11 = -1.5, i.e. 4 = 10]
print(temp)
print()
selected_temp = selected_month
print_statement = "The average temperature in Helsinki in " + str(months[selected_month]) + " is " + str(
    average_temp[selected_temp])
print(print_statement)
# Additional tests
assert len(months) == 12, 'Right length!'
assert len(average_temp) == 12, 'Right length!'
assert isinstance(months, list), 'Variable months is  a list'
assert isinstance(average_temp, list), 'Variable average_temp is a list'
assert print_statement == 'The average temperature in Helsinki in July is 18.0'
# Problem 3 Markdown text
'''i learnt a lot. Separating names using the input function was unclear.I would change that part of separating 
names '''



