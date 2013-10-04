# Multiply all the elements in a list

n = [2,4,6,9,10]

p = 8

def multiply_list(l):
    if l == []:
        return 1

    return l[0] * multiply_list(l[1:])

print multiply_list(n)

def factorial(l):
    import math

    if l == 0:
        return 0

    return l * math.factorial(l-1)

print factorial(p) 


# Count the number of elements in the list l
def count_list(l):
    if l == []:
        return 0
    return 1 + count_list(l[1:])

print count_list(n)

# Sum all of the elements in a list
def sum_list(l):
    if l == []:
        return 0

    return l[0] + sum_list(l[1:])

print sum_list(n)

# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 0:
        return []

    return [l[-1]] + reverse(l[:-1])

print reverse(n)


# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 2:
        return 1

    first = fibonacci(n-2)
    second = fibonacci(n-1)
    return first + second    

print fibonacci(p)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l == []:
        return None
    if l[0] == i:
        return i
    else:
        return find(l[1:], i)

print find(n, 10)

# Determines if a string is a palindrome
def palindrome(some_string):
    # if len(some_string) == 0:
    #     return False

    # if some_string[0] != some_string[-1]:
    #     return False
    # else:
    #     return palindrome(some_string[1:-1])

    if some_string == "":
        return True
    elif len(some_string) == 1:
        return True
    return some_string[0] == some_string[-1] and palindrome(some_string[1:-1])


#print palindrome("A man a plan a canal Panama")

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)

    if width > height:
        return fold_paper(width/2, height, folds-1)
    else:
        return fold_paper(width, height/2, folds-1)

#print fold_paper(80, 100, 10)




# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    count = range(n, target + 1)
    if count == []:
        return 0
    
    num = count.pop(0)

    print num

    return count_up(target, n+1)

count_up(10, 0)



