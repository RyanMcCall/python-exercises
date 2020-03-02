import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
a_negative = a[a < 0]

count_negative_in_a = len(a_negative)

assert count_negative_in_a == 4

# How many positive numbers are there?
a_positive = a[a > 0]

count_positive_in_a = len(a_positive)

assert count_positive_in_a == 5

# How many even positive numbers are there?
a_even_positive = a_positive[a_positive % 2 == 0]

count_even_positive = len(a_even_positive)

assert count_even_positive == 3

# If you were to add 3 to each data point, how many positive numbers would there be?
