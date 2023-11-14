def exp1(a, b):
    if b == 1:
        return a
    else:
        return a * exp1(a, b - 1)
    
# Execução
resultado = exp1(2, 3)
print(resultado)