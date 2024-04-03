import numpy as np

# a = np.array([1, 2, 3, 4, 5])

# print(a)
# print(type(a))
# print(a[:3])
# print(a[-1])
# print(a[4])


# a_mul = np.array(
#     [
#         [1, 2, 3],
#         [1, 4, 7],
#         [8, 1, 3],
#     ]
# )

# print(a_mul[0])
# print(a_mul[0, 1])
# print(a_mul[1, 2])
# print(a_mul[2, 1])
# print(a_mul.shape)


# a_mul = np.array(
#     [
#         [
#             [1, 2, 3],
#             [1, 4, 7],
#             [8, 1, 3],
#         ],
#         [
#             [1, 2, 3],
#             [1, 4, 7],
#             [8, 1, 3],
#         ],
#     ]
# )

# print(a_mul[0][0, 1])
# print(a_mul.shape)
# print(a_mul.ndim)
# print(a_mul.size)
# print(a_mul.dtype)


a = np.full((3, 3, 4), 10)
print(a)
