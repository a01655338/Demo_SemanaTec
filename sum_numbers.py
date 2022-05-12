"""
Program to sum all the numbers from 1 to 100
Using a while loop

Gilberto Echeverria
gilecheverria@yahoo.com
27/02/2018
"""

def sum_to_N(limit):
    """ Sum all the numbers from 1 to limit """
    total = 0
    for i in range(1, limit+1):
        total += i
    return total

limit = int(input("Enter the number to sum up to: "))
print(f"The total sum is: {sum_to_N(limit)}")
