# Entendimento:
Ler o número de horas trabalhadas no mês (variável HT).
Ler o valor da hora-aula (variável VH).
Ler o percentual de desconto do INSS (variável PD).
Calcular o salário bruto (SB) multiplicando as variáveis HT e VH.
Calcular o total de desconto (TD) com base no valor de PD dividido por 100.
Calcular o salário líquido (SL) deduzindo o desconto do salário bruto (SB).
Apresentar os valores dos salários bruto e líquido (SB e SL).

# Diagramação (Diagrama de Bloco):
O diagrama de bloco representa a sequência de ações a serem executadas.
img = Image.open("img/salario-professor.png")

# Português Estruturado (Codificação):
programa SALARIO_PROFESSOR
var
    HT: inteiro
    VH, PD, TD, SB,SL: real

inicio
    leia HT, VH, PD
    SD = HT * VH
    TD = (PD / 100) * SB
    SL = SB - TD
    escreva SB, SL
fim
