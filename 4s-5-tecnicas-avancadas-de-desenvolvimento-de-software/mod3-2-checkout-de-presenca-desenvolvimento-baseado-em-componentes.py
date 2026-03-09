# Calculadora Simples com Componentes Reutilizáveis

# importação das bibliotecas
import click # biblioteca Python que facilita a criação de interfaces de linha de comando (CLI

# componente para adição
def add(a, b):
    # função de adição
    return a + b

# componente para subtração
def subtract(a, b):
    # função de subtração
    return a - b

# componente para multiplicação
def multiply(a, b):
    # função de multiplicação
    return a * b

# componente para divisão
def divide(a, b):
    # função de divisão
    if b == 0:
        return "Erro ao dividir por zero."
    return a / b

# Interface de linha de comando
@click.command()
@click.option('--operation', type=click.Choice(['add', 'subtract', 'multiply', 'divide']), help="Operação (add, subtract, multiply, divide).")
@click.option('--a', type=float, help="Primeiro número.")
@click.option('--b', type=float, help="Segundo número.")
def calculator(operation, a, b):
    # Calculadora simples.
    if operation == 'add':
        result = add(a, b)
    elif operation == 'subtract':
        result = subtract(a, b)
    elif operation == 'multiply':
        result = multiply(a, b)
    elif operation == 'divide':
        result = divide(a, b)
    else:
        result = "Cálculo inválido."

    click.echo(f"Resultado: {result}")

if __name__ == '__main__':
    
    # Exemplos de execução direta
    print("=== Exemplos de Cálculos ===")
    print(f"Adição (10 + 5): {add(10, 5)}")
    print(f"Subtração (10 - 5): {subtract(10, 5)}")
    print(f"Multiplicação (10 * 5): {multiply(10, 5)}")
    print(f"Divisão (10 / 5): {divide(10, 5)}")
    print(f"Divisão (10 / 0): {divide(10, 0)}")
    print("\n")
    
    # Executa a interface CLI se parâmetros forem passados
    calculator()