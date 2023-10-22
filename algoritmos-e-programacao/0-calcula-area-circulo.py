# Entendimento:
Ler um valor para o raio, representado pela variável R.
Definir a constante π com o valor 3.14159265.
Calcular a área, elevando o valor de R ao quadrado e multiplicando-o por π.
Apresentar o valor da área (variável A).

# Diagramação (Diagrama de Bloco):
O diagrama de bloco representa a sequência de ações a serem executadas.
img = Image.open("img/calcular-area-circulo.png")

# Português Estruturado (Codificação):
programa AREA_CIRCULO

const
    PI: real = 3.14159265
var
    A: real
    B: real

inicio
    leia R
    A = PI * R * R
    escreva A
fim