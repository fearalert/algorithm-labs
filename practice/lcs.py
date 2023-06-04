def longest_common_subsequence(A, B):
    m = len(A)
    n = len(B)

    # Create tables for dynamic programming
    prev = [[0] * (n + 1) for _ in range(m + 1)]
    length = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the tables using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                length[i][j] = length[i - 1][j - 1] + 1
                prev[i][j] = "diagonal"
            else:
                if length[i - 1][j] >= length[i][j - 1]:
                    length[i][j] = length[i - 1][j]
                    prev[i][j] = "up"
                else:
                    length[i][j] = length[i][j - 1]
                    prev[i][j] = "left"

    # Retrieve the LCS
    lcs = []
    i = m
    j = n
    while i > 0 and j > 0:
        if prev[i][j] == "diagonal":
            lcs.append(A[i - 1])
            i -= 1
            j -= 1
        elif prev[i][j] == "up":
            i -= 1
        else:
            j -= 1

    # Reverse the LCS to get the correct order
    lcs.reverse()

    return lcs

#Driver code
A = "president"
B = "providence"
result = longest_common_subsequence(A, B)
print("Longest Common Subsequence of ", A, "and", B,"is:" ,"".join(result))
