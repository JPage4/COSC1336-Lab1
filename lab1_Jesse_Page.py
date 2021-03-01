#Jesse Page
#Lab 1 assignment             
#This program will take prompt the user to enter their name and birth month and year.
#The program will then output to the console a greeting with their name, what season they were born, 
# and whether or not they were born in a leap year.

#variables storing the user's input
userName = input("Please enter your name: ")
userBdayMonth = int(input("Please enter the month you were born as an integer, ex: December = 12: "))
userBdayYear = int(input("Please enter the year you were born, ex: 1989: "))
season = "fall"

#if-else condition to check userBdayMonth and assign correct season
if userBdayMonth > 12 or userBdayMonth <= 0:
    season = "Invalid month"
elif userBdayMonth <= 2:
    season = "winter"
elif userBdayMonth <= 5:
    season = "spring"
elif userBdayMonth <= 8:
    season = "summer"
elif userBdayMonth <= 11:
    season = "fall"
elif userBdayMonth == 12:
    season = "winter"
else:
    season = "Invalid month"

#if-else condition to check if userBdayYear is a leap year, and the resulting print statement
if userBdayYear % 4 == 0 and (userBdayYear % 400 == 0 or userBdayYear % 100 != 0):
    print("Hello,", userName, end="")
    print("! You were born in the", season, end="")
    print(".",userBdayYear, "was a leap year.", end="")
else:
    print("Hello,", userName, end="")
    print("! You were born in the", season, end="")
    print(".",userBdayYear, "was not a leap year.", end="")    

