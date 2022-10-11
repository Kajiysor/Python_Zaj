import random

numbers = random.sample(range(0, 100), 10)

print(numbers)

print(''.join(str(num) for num in numbers))
