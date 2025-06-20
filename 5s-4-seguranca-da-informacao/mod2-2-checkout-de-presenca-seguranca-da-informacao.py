def cifra_cesar(texto, deslocamento, operacao):
    resultado = ""
 
    for letra in texto:
        if letra.isalpha():
            base = ord("A") if letra.isupper() else ord("a")
            if operacao == "criptografar":
                nova_letra = chr((ord(letra) - base + deslocamento) % 26 + base)
            else:
                nova_letra = chr((ord(letra) - base - deslocamento) % 26 + base)
            resultado += nova_letra
        else:
            resultado += letra
    return resultado

print("=== Cifra de César Simples ===")
print("1. Criptografar")
print("2. Descriptografar")

opcao = input("Escolha (1/2): ")
texto = input("Digite o texto: ")
deslocamento = int(input("Deslocamento (1-25): "))

if opcao == "1":
    print("Texto criptografado:", cifra_cesar(texto, deslocamento, "criptografar"))
else:
    print("Texto descriptografado:", cifra_cesar(texto, deslocamento, "descriptografar"))