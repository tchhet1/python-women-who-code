#Write a program that inputs two natural numbers from the user and displays their GCD, 
# also known as the highest common factor (HCF).
input_one = int(input("Enter a number: "))
input_two = int(input("Enter another number: "))

# 30, 13
remainder = 1
number = 0
if(input_one > input_two):
    remainder = input_one % input_two
    #4 = 30 % 13
    number = input_two
    #number = 13
else:
    remainder = input_two % input_one
    number = input_one


while(remainder != 0):

    temp = remainder
    # temp = 4, 1
    remainder = number % remainder
    #remainder = 13 % 4 -> 1
    number = temp
    #number = 4
    
print(number)
