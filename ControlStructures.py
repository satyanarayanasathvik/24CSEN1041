#Check whether a given integer number is a 3-digit number.

num = int(input("Enter any number: "))

if(num>=100 and num<=999):
    print("Number of digits is 3")
else:
    print("Number of digits is not 3")


num = int(input("Enter any number: "))
count = 0

while(num != 0):
    count += 1
    num //= 10

if(count == 3):
    print("Number of digits is 3")
else:
    print("Number of digits is not 3")


#Given an integer number, if it is a 3-digit number, then find out its last digit. Otherwise, display its last but one digit.
num = int(input("Enter any number: "))

if(num>=100 and num<=999):
    print(num%10)
else:
    num //= 10
    print(num%10)

#While purchasing certain items, a discount of 10% is offered if the purchased quantity is more than 1000. Otherwise, there is no discount.
#The quantity and price per item are given as inputs. Compute the total expenses.

