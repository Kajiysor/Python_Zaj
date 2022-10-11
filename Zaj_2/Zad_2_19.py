import random

num = "12"

one_num = random.sample(range(1, 10), 3)
two_num = random.sample(range(1, 100), 3)
three_num = random.sample(range(1, 1000), 3)

all_num = one_num + two_num + three_num

print(all_num)

filled_nums = []

for i in all_num:
    filled_nums.append(str(i).zfill(3))

print(filled_nums)
