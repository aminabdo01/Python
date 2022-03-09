# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Days_left = (365 * 90) - (int(age) * 365) 
Weeks_left = (52 * 90) - (int(age) * 52) 
Months_left = (12 * 90) - (int(age) * 12)

print("You have {Days_left} days, {Weeks_left} weeks, and {Months_left} months left.")