import string


def encrypt_caesar():
    alphabet = list(string.ascii_lowercase)
    word = input("Enter the word: ")
    word_list = list(word)
    shift_time = int(input("Enter how much you want to shift: "))
    for i in range(len(word_list)):
        x = word_list[i]

        for j in range(len(alphabet)):

            if x == alphabet[j]:
                shift = j + shift_time
                if shift > 26:
                    mod = shift - 26
                    print(alphabet[mod], end="")
                else:
                    print(alphabet[shift], end="")


# encrypt_caesar()
# list.sort()


# def second_min_max(listA):
#     for i in range(len(listA) - 1):
#         temp = listA[i]

#         temp_val = 0
#         for j in range(len(listA) - 2):
#             if temp > listA[j + 1]:
#                 print("oh yeah")
#                 print(listA[j + 1])
#                 temp_val = listA[j + 1]
#                 listA[j + 1] = temp
#                 temp_val = temp

#             print(listA[j])


# second_min_max(listA=[4, 7, 1, 5, 3])
