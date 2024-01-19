# user input name/age
user_name = input("What is your name? ")  # get name as str
user_age = int(input("How old are you? "))  # get age as int
user_birth_year = 2024 - user_age  # calculate birth year

print(f"Hello {user_name}! You were born in {user_birth_year}.")  # print greeting
