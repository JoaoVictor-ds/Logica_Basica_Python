numeros = []

for i in range(3):
    while True:
        try:
            numero_in = int(input(f"Informe o {i+1}º número inteiro: "))
            numeros.append(numero_in)
            break  # sai do loop interno após entrada válida
        except ValueError:
            print("Entrada inválida, tente novamente com um número inteiro.")

print("O maior número da sequência é:", max(numeros))
print("O menor número da sequência é:", min(numeros))
