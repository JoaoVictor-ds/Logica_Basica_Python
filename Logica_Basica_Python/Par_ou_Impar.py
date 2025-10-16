"""
Embora não seja necessário, decidir aplicar a lógica de ter um módulo "main" aqui.
passei um tempo estudando JAVA na faculdade e acabei gostando ;)

"""

def par_ou_impar(numero_inteiro):
    if numero_inteiro % 2 == 0:
        print("Este é um número par")
    else:
        print("Este é um número ímpar")

def main():
    while True:
        try:
            numero = int(input("Informe um número inteiro: "))
            par_ou_impar(numero)
            break  # encerra o loop após entrada válida
        except ValueError:
            print("Entrada inválida, insira um número inteiro.")

main()

