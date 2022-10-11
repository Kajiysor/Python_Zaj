example_line = """ this is a very
        long string if I had the
        energy to type more and more ..."""

longest_string = max(example_line.split(), key=len)

print(f"Longest string: {longest_string}, longest string length: {len(longest_string)}")