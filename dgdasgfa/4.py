#Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci. Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
contar = 0
def fibo(n):
    global contar
    contar +=1
    if n <= 1:
        return n
    else:
        return fibo(n-1)+(n-2)
print(fibo(21))
print(contar)