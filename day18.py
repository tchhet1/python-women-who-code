#Create a program to find the largest among three numbers.

#soltuion 1
def findLargestNum(num1, num2, num3):
    return max(num1, num2, num3)

findLargestNum(2, 4, 10)


# solution 2
def findLargestNum2(num1, num2, num3):
    if(num1 >= num2 and num1 >= num3):
        largestNum = num1
    elif(num2 >= num3 and num2 >= num1):
        largestNum = num2
    else:
        largestNum = num3
    print("largest num: ", largestNum)
    return largestNum

findLargestNum2(2, 4, 8)