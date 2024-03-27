# def even_odd():
#     num = int(input("Enter a number to check even or odd: "))
#     if num % 2 == 0:
#         return f"{num} is even"
#     else:
#         return f"{num} is odd"


# print(even_odd())


# num_list = [156, 200, 1, 0, 500, 6, 4, 66]


# def max_num(num_list):

#     temp_max = num_list[0]
#     for i in range(len(num_list) - 1):
#         if temp_max < num_list[i]:
#             temp_max = num_list[i]
#     return temp_max


# print(max_num(num_list))


# def min_num(num_list):

#     temp_min = num_list[0]
#     for i in range(len(num_list) - 1):
#         if temp_min > num_list[i]:
#             temp_min = num_list[i]
#     return temp_min


# print(min_num(num_list))


# def table():
#     num = int(input("Enter a number to calculate its table: "))
#     table_limit = int(input("Enter a limit for table table: "))
#     for i in range(1, table_limit + 1):
#         table = f"{num} * {i} = {num * i}"
#         print(table)


# table()


# def facto(fact):

#     if fact == 0 or fact == 1:
#         return 1
#     else:
#         return fact * facto(fact - 1)


# print(facto(1))


# sequence = [1, 5, 10, 100]


# def sum_of_sequence(sequence):
#     sum = 0
#     for i in sequence:
#         sum += i
#     return sum


# print(sum_of_sequence(sequence))


# def ascending():
#     limit = int(input("Enter Limit to generate ascending number: "))
#     for i in range(0, limit + 1):
#         print(i)


# ascending()


# def descending():
#     limit = int(input("Enter Limit to generate descending number: "))
#     for i in range(limit, 0, -1):
#         print(i)


# descending()

# import math


# def area_of_circle():
#     radius = int(input("Enter radius of circle: "))
#     area = math.pi * pow(radius, 2)
#     return area


# print(area_of_circle())


# def celsius_to_fahrenheit():
#     celsius = int(input("Enter value in celsisus unit: "))
#     fahrenheit = (celsius * (9 / 5)) + 32
#     return fahrenheit


# print(celsius_to_fahrenheit())


# def fahrenheit_to_celsius():
#     fahrenheit = int(input("Enter value in fahrenheit unit: "))
#     celsius = ((fahrenheit) - 32) * (5 / 9)
#     return celsius


# print(celsius_to_fahrenheit())


# def sum_positive_integer(n):
#     sum = (n * (n + 1)) / 2
#     return sum


# print(sum_positive_integer(4))

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
