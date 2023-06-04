def brute_force_pattern_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            return i

    return -1

text = "Hello, world!"
pattern = "w"
result = brute_force_pattern_match(text, pattern)
if result != -1:
    print(f"Pattern '{pattern}' found at index {result} in the text.")
else:
    print(f"Pattern '{pattern}' not found in the text.")
