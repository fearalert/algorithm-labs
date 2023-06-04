import sys

def matrix_chain(p, n):
    m = [[0] * n for _ in range(n)]  # Create an n x n matrix to store results
    
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize  # Initialize m[i][j] to a large value
            
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    
    return m[1][n - 1]

# Test the matrix_chain function
p = [5, 10, 3, 12, 5, 50, 6]
n = len(p)

optimal_cost = matrix_chain(p, n)
print("Optimal Cost:", optimal_cost)
