# valor e dois ponteiros para seus filhos esquerdo (fe) e direito (fd).
class no:
    def __init__(self, valor):
        self.valor = valor
        self.fe = None
        self.fd = None

# retorna o valor do nó mais à esquerda.  
def menor(raiz):
    if raiz is None:
        return None
    
    atual = raiz
    while atual.fe is not None:
        atual = atual.fe
        
    return atual.valor
        
# Teste
raiz = no(7)
raiz.fd = no(10)
print(menor(raiz))

raiz = no(47)
raiz.fe = no(40)
raiz.fe.fe = no(30)
raiz.fe.fe.fd = no(36)
raiz.fe.fd = no(45)
raiz.fd = no(58)
raiz.fd.fe = no(50)
raiz.fd.fd = no(60)
print(menor(raiz))