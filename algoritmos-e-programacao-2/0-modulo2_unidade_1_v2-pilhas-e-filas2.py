# Definição da classe Banco para gerenciamento de filas
class Banco:
    def __init__(self):
        # Inicialização das filas prioritárias e normais
        self.fila_prioritaria = []  # Fila prioritária
        self.fila_normal = []       # Fila normal

    def entrar_na_fila(self, nome, idade):
        # Método para adicionar pessoas às filas com base na idade
        if idade > 60:
            # Se a idade for maior que 60, a pessoa entra na fila prioritária
            self.fila_prioritaria.append((nome, idade))
        else:
            # Caso contrário, a pessoa entra na fila normal
            self.fila_normal.append((nome, idade))

    def sair_da_fila(self):
        # Método para simular a saída de pessoas das filas
        if self.fila_prioritaria:
            # Verifica se há pessoas na fila prioritária
            pessoa = self.fila_prioritaria.pop(0)
            # Remove a primeira pessoa da fila prioritária
            print(f"{pessoa[0]} (idade {pessoa[1]}) saiu da fila Prioritária.")
            if len(self.fila_prioritaria) % 2 == 0:
                # Se o tamanho da fila prioritária for par após a saída, verifica se há pessoas na fila normal
                if self.fila_normal:
                    pessoa_normal = self.fila_normal.pop(0)
                    # Remove a primeira pessoa da fila normal
                    print(f"{pessoa_normal[0]} (idade {pessoa_normal[1]}) saiu da fila normal.")

    def status_filas(self):
        # Método para exibir o status atual das filas
        print(f"Fila Prioritária: {[p[0] for p in self.fila_prioritaria]}")
        print(f"Fila Normal: {[p[0] for p in self.fila_normal]}")

# Exemplo de uso:
banco = Banco()

# Inserindo pessoas nas filas
banco.entrar_na_fila("João", 65)
banco.entrar_na_fila("Maria", 55)
banco.entrar_na_fila("Pedro", 70)
banco.entrar_na_fila("Ana", 50)
banco.entrar_na_fila("Rose", 50)
banco.entrar_na_fila("Jamily", 50)

# Exibindo status das filas
banco.status_filas()

# Simulando a saída de pessoas
banco.sair_da_fila()
banco.sair_da_fila()
banco.sair_da_fila()

# Exibindo status das filas após a saída
banco.status_filas()
