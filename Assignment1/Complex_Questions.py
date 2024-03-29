# import string


# def encrypt_caesar():
#     alphabet = list(string.ascii_lowercase)
#     word = input("Enter the word: ")
#     word_list = list(word)
#     shift_time = int(input("Enter how much you want to shift: "))
#     for i in range(len(word_list)):
#         x = word_list[i]

#         for j in range(len(alphabet)):

#             if x == alphabet[j]:
#                 shift = j + shift_time
#                 if shift > 26:
#                     mod = shift - 26
#                     print(alphabet[mod], end="")
#                 else:
#                     print(alphabet[shift], end="")


# encrypt_caesar()


# def second_min_max(listA):
#     listA.sort()
#     print(listA)
#     sec_max = listA[-2]
#     sec_min = listA[1]
#     print(f"Second Maximum:{sec_max}")
#     print(f"Second Minimum:{sec_min}")


# second_min_max(listA=[4, 7, 1, 5, 3])


import string


def encrypt_caesar():
    """
    Encrypts a given word using the Caesar cipher with a specified shift value.

    Prompts the user to input a word and the desired shift value, then prints the encrypted word.

    Parameters:
    None

    Returns:
    None
    """
    try:
        alphabet = list(string.ascii_lowercase)
        word = input("Enter the word: ")
        word_list = list(word)
        shift_time = int(input("Enter how much you want to shift: "))
        encrypted_word = ""

        for i in range(len(word_list)):
            x = word_list[i]
            for j in range(len(alphabet)):
                if x == alphabet[j]:
                    shift = j + shift_time
                    if shift > 25:
                        mod = shift - 26
                        encrypted_word += alphabet[mod]
                    else:
                        encrypted_word += alphabet[shift]

        print("Encrypted word:", encrypted_word)
    except ValueError:
        print("Error: Shift value must be an integer.")


encrypt_caesar()


def second_min_max(listA):
    """
    Finds the second minimum and maximum elements from a list of integers.

    Sorts the list, then prints the second minimum and second maximum elements.

    Parameters:
    listA (list): The input list of integers.

    Returns:
    None
    """
    try:
        if len(listA) < 2:
            print("Error: List must contain at least two elements.")
            return

        listA.sort()
        sec_max = listA[-2]
        sec_min = listA[1]

        print("Sorted list:", listA)
        print(f"Second Maximum: {sec_max}")
        print(f"Second Minimum: {sec_min}")
    except TypeError:
        print("Error: Input must be a list of integers.")


second_min_max(listA=[4, 7, 1, 5, 3])

# Test cases
# Test case for encrypt_caesar() with valid inputs
# Input: word = "hello", shift_time = 3
# Expected Output: "Encrypted word: khoor"
encrypt_caesar()

# Test case for encrypt_caesar() with non-integer shift value
# Input: word = "hello", shift_time = "abc"
# Expected Output: "Error: Shift value must be an integer."
encrypt_caesar()

# Test case for second_min_max() with valid input list
# Input: listA = [4, 7, 1, 5, 3]
# Expected Output: "Sorted list: [1, 3, 4, 5, 7]", "Second Maximum: 5", "Second Minimum: 3"
second_min_max(listA=[4, 7, 1, 5, 3])

# Test case for second_min_max() with empty input list
# Input: listA = []
# Expected Output: "Error: List must contain at least two elements."
second_min_max(listA=[])

# Test case for second_min_max() with non-integer elements in input list
# Input: listA = [4, 7, "abc"]
# Expected Output: "Error: Input must be a list of integers."
second_min_max(listA=[4, 7, "abc"])
