# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def twoSum(nums, target):
    for index, num in enumerate(nums):
        difference = target - num
        try:
            targetIndex = nums[index + 1:].index(difference) + index + 1
            print(targetIndex)
            print([index, targetIndex])
            return [index, targetIndex]
        except ValueError:
            continue

    return "hey"

twoSum([3, 2, 4], 6)