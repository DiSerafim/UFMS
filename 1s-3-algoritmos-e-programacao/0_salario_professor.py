from PIL import Image

### Entendimento:
# Ler o número de horas trabalhadas no mês (variável HT).
# Ler o valor da hora-aula (variável VH).
# Ler o percentual de desconto do INSS (variável PD).
# Calcular o salário bruto (SB) multiplicando as variáveis HT e VH.
# Calcular o total de desconto (TD) com base no valor de PD dividido por 100.
# Calcular o salário líquido (SL) deduzindo o desconto do salário bruto (SB).
# Apresentar os valores dos salários bruto e líquido (SB e SL).

### Diagramação (Diagrama de Bloco):
# O diagrama de bloco representa a sequência de ações a serem executadas.
img = Image.open("img/salario-professor.png")

### Português Estruturado (Codificação):
# programa SALARIO_PROFESSOR
# var
#     HT: inteiro
#     VH, PD, TD, SB,SL: real

# inicio
#     leia HT, VH, PD
#     SD = HT * VH
#     TD = (PD / 100) * SB
#     SL = SB - TD
#     escreva SB, SL
# fim

# Entrada de dados
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
valor_hora_aula = float(input("Informe o valor da hora-aula: "))
percentual_desconto = float(input("Informe o percentual de desconto do INSS: "))

# Cálculo do salário bruto
salario_bruto = horas_trabalhadas * valor_hora_aula

# Cálculo do total de desconto
total_desconto = (percentual_desconto / 100) * salario_bruto

# Cálculo do salário líquido
salario_liquido = salario_bruto - total_desconto

# Saída de dados
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")