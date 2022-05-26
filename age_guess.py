# Simple program to guess the user's age based off their birth year

# importing date class from datetime module
from datetime import date

birth_year = input("What year were you born? ")

# creating the date object of today's date
todays_date = date.today()

# Displaying the current age based on current year compared to birth_year
print("You are", todays_date.year - int(birth_year), "years old!")