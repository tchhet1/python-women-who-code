# Create a program that swaps the values of two variables.

#using temporary variable
def swap_variable(a, b):

    c = a
    a = b
    b = c
    return a, b

result = swap_variable(10, 5)
print(result)

#without using temporary variable

