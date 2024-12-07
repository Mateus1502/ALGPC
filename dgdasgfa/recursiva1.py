#Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N#
def somatorio(n):
    if n == 1:
        return 1
    return n + somatorio(n - 1)

n = int(input("Informe um número: "))
resultado = somatorio(n)
print("O somatório de 1 até", n, "é:", resultado)