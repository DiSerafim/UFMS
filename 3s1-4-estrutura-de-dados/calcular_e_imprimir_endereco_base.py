def calcular_e_imprimir_endereco_base(chaves, M):
    enderecos = []
    
    for chave in chaves:
        endereco = chave % M
        enderecos.append((chave, endereco))
        
    return enderecos

def main():
    # Ler valores de entrada
    K, M = map(int, input().split())
    
    chaves = []
    
    for _ in range(K):
        chave = int(input())
        chaves.append(chave)
        
    enderecos = calcular_e_imprimir_endereco_base(chaves, M)
    
    # Imprime os resultados
    for chave, endereco in enderecos:
        print(f"{chave} -> {endereco}")
        
if __name__ == "__main__":
    main()