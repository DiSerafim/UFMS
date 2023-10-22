from PIL import Image

# Entendimento:
Ler dois valores inteiros (A e B).
Efetuar a adição dos valores A e B.
Apresentar o resultado da soma.

# Diagramação (Diagrama de Bloco):
O diagrama de bloco é representado graficamente como um fluxo de ações a serem realizadas. Os blocos de ação incluem entrada de dados, processamento e saída.

img = Image.open("img/soma-numeros-diagrama.png")

# Português Estruturado (Codificação):
programa SOMA_NUMEROS

var
    X: inteiro
    A: inteiro
    B: inteiro

inicio
    leia A
    leia B
    X = A + B
    escreva X
fim

