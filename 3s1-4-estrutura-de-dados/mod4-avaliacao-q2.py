def grau(M, n, v):
    if v < 0 or v >= n:
        raise ValueError("Inválido")
    
    degree = 0
    for neighbor in range(n):
        if M[v][neighbor] == 1:
            degree += 1
    
    return degree

# Example usage
M = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0]
]

n = 5
v = 1

degree = grau(M, n, v)
print(f"grau v {v}: {degree}")