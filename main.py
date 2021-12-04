# Average Rainfall
# Write a program that uses nested loops to collect data and
# calculate the average rainfall over a period of years.

# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches
# of rainfall for that month. After all iterations, the program should
# display the number of months, the total inches of rainfall,
# and the average rainfall per month for the entire period.


# The program should first ask for the number of years.
num_of_years = int(input("Enter the number of years: "))
rainfall = 0

for year in range(1, num_of_years + 1): #The outer loop will iterate once for each year.
    for month in range(1, 13): # The inner loop will iterate twelve times, once for each month.
        prompt = 'Enter number of inches of rainfall for month ' + str(month) + ' of year ' + str(year) + ':'
        rainfall += float(input(prompt))

        num_months = num_of_years * 12
        avg_rainfall = rainfall / num_months

print("\nThe total amount of rainfall during these", int(num_months), "months was", format(rainfall, ".1f"))
print("The average rainfall per month was " + format(avg_rainfall, ".1f") + " inches")

