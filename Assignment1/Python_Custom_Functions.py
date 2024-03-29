# Function: even_odd()
# Test cases:
# Test Case 1: Test with an even number
# Expected Output: "156 is even"
# Test Case 2: Test with an odd number
# Expected Output: "7 is odd"
# Test Case 3: Test with zero
# Expected Output: "0 is even"
# Test Case 4: Test with a negative odd number
# Expected Output: "-9 is odd"
# Test Case 5: Test with a negative even number
# Expected Output: "-22 is even"
def even_odd():
    num = int(input("Enter a number to check even or odd: "))
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"


print(even_odd())

# Function: max_num()
# Test cases:
# Test Case 1: Test with positive numbers
# Expected Output: 500
# Test Case 2: Test with negative numbers
# Expected Output: -4
# Test Case 3: Test with a mixture of positive and negative numbers
# Expected Output: 200
# Test Case 4: Test with a list containing only one element
# Expected Output: 100
# Test Case 5: Test with an empty list
# Expected Output: None

num_list = [156, 200, 1, 0, 500, 6, 4, 66]


def max_num(num_list):

    temp_max = num_list[0]
    for i in range(len(num_list) - 1):
        if temp_max < num_list[i]:
            temp_max = num_list[i]
    return temp_max


print(max_num(num_list))


# Function: min_num()
# Test cases:
# Test Case 1: Test with positive numbers
# Expected Output: 0
# Test Case 2: Test with negative numbers
# Expected Output: -4
# Test Case 3: Test with a mixture of positive and negative numbers
# Expected Output: -4
# Test Case 4: Test with a list containing only one element
# Expected Output: 100
# Test Case 5: Test with an empty list
# Expected Output: None


def min_num(num_list):

    temp_min = num_list[0]
    for i in range(len(num_list) - 1):
        if temp_min > num_list[i]:
            temp_min = num_list[i]
    return temp_min


print(min_num(num_list))

# Function: table()
# No specific test cases provided. The function takes user input.


def table():
    num = int(input("Enter a number to calculate its table: "))
    table_limit = int(input("Enter a limit for table table: "))
    for i in range(1, table_limit + 1):
        table = f"{num} * {i} = {num * i}"
        print(table)


table()


# Function: table()
# No specific test cases provided.
def facto(fact):

    if fact == 0 or fact == 1:
        return 1
    else:
        return fact * facto(fact - 1)


print(facto(1))

# Function: table()
# No specific test cases provided.

sequence = [1, 5, 10, 100]


def sum_of_sequence(sequence):
    sum = 0
    for i in sequence:
        sum += i
    return sum


print(sum_of_sequence(sequence))

# Function: table()
# No specific test cases provided.


def ascending():
    limit = int(input("Enter Limit to generate ascending number: "))
    for i in range(0, limit + 1):
        print(i)


ascending()

# Function: table()
# No specific test cases provided.


def descending():
    limit = int(input("Enter Limit to generate descending number: "))
    for i in range(limit, 0, -1):
        print(i)


descending()

import math

# Function: table()
# No specific test cases provided.


def area_of_circle():
    radius = int(input("Enter radius of circle: "))
    area = math.pi * pow(radius, 2)
    return area


print(area_of_circle())


# Function: table()
# No specific test cases provided.


def celsius_to_fahrenheit():
    celsius = int(input("Enter value in celsisus unit: "))
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit


print(celsius_to_fahrenheit())

# Function: table()
# No specific test cases provided.


def fahrenheit_to_celsius():
    fahrenheit = int(input("Enter value in fahrenheit unit: "))
    celsius = ((fahrenheit) - 32) * (5 / 9)
    return celsius


print(celsius_to_fahrenheit())

# Function: table()
# No specific test cases provided.


def sum_positive_integer(n):
    sum = (n * (n + 1)) / 2
    return sum


print(sum_positive_integer(4))

# Function: linear_search()
# Test cases:
# Test Case 1: Test with a number present in the list
# Expected Output: 7
# Test Case 2: Test with a number not present in the list
# Expected Output: -1
# Test Case 3: Test with the first element of the list
# Expected Output: 0
# Test Case 4: Test with the last element of the list
# Expected Output: 7
# Test Case 5: Test with an empty list
# Expected Output: -1

listA = [4, 1, 8, 3, 9, 6, 7, 100]


def linear_search(listA, num):
    temp = -1
    x = num
    for i in range(len(listA)):
        if x == listA[i]:
            temp = i
            break
    return temp


print(linear_search(listA, 100))
