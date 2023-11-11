# A função abaixo resolve o problema do Fatorial utilizando a recursividade.

def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat( n-1 )
    
    
resultado = fat(1)
print(resultado)

# a. A condição n==1 representa a condição de saída da recursividade.
