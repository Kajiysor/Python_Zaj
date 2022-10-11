example_line = """ this is a very
        long string if I had the
        energy to type more and more ..."""

first_char_word = []
last_char_word = []

for i in example_line.split():
    first_char_word.append(i[0])
    last_char_word.append(i[-1])

print(f"First char word: {''.join(first_char_word)}")
print(f"Last char word: {''.join(last_char_word)}")
