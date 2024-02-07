#Write a function to calculate the factorial of a number.
# 5 = 5*4*3*2*1

#solution 1
def factorial(num):
    result = 1
    for i in range(num, 1, -1):
        result = result * i
    print(result)
    return result

factorial(5)

#solution 2 using recurion
def factorial1(n):
    if(n == 0 or n ==1):
        return 1
    else:
        print("n: ", n)
        return n * factorial1(n - 1)
    
result = factorial1(5)
print(result)
