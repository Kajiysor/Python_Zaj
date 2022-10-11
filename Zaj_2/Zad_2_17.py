example_line = """ this is a very
        long string if I had the
        energy to type more and more ..."""

print(f"Sorted alphabetically: {sorted(example_line.split())}")
print(f"Sorted by length: {sorted(example_line.split(), key=len)}")

