import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
a_negative = a < 0

count_negative_in_a = a_negative.sum()

assert count_negative_in_a == 4

# How many positive numbers are there?
a_positive = a > 0

count_positive_in_a = a_positive.sum()

assert count_positive_in_a == 5

# How many even positive numbers are there?
a_even_positive = a[a_positive] % 2 == 0

count_even_positive = a_even_positive.sum()

assert count_even_positive == 3

# If you were to add 3 to each data point, how many positive numbers would there be?
a_add_3_positive = (a + 3) > 0

count_add_3_positive = a_add_3_positive.sum()

assert count_add_3_positive == 10

# If you squared each number, what would the new mean and standard deviation be?
