
age = input('What is your current age?')
#Convert the age variable to a number and save it to this variable
age_as_int = int(age)
#We are subtracting our goal age of 90 by what the user inputs, and this is the years left to reach 90
years_remaining = 90 - age_as_int
#We are taking the user's years_remaining and multiplying it by the # of days in a year
days_remaining = years_remaining * 365
#We are taking the user's years_remaining and multiplying it by the # of weeks in a year
weeks_remaining = years_remaining * 52
#We are taking the user's years_remaining and multiplying it by the # of months in a year
months_remaining = years_remaining * 12
#Save the message we want to display in a var named message 
message = f'You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left before you reach the age of 90.'
#print message
print(message)