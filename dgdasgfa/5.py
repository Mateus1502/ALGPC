#Torres de Hanói é um jogo matemático onde dispomos de 3 pinos: pino origem, pino de trabalho e pino destino. O pino origem contém n discos empilhados por ordem crescente de tamanho (o maior disco fica embaixo). O objetivo do jogo é levar todos os discos do pino origem para o pino destino, utilizando o pino de trabalho para auxiliar a tarefa, e atendendo às seguintes restrições:

#Apenas um disco pode ser movido por vez (o disco que estiver no topo da pilha de um dos pinos).
#Um disco de tamanho maior nunca pode ser colocado sobre um disco de tamanho menor.
#Faça um programa com função recursiva que resolve o jogo das Torres de Hanoi.
mov =0
def hanoi(qtde,origem,destino,aux):
    global mov
    mov +=1
    if qtde >= 1:
        hanoi(qtde-1,origem,aux,destino)
        print(f"Mover disco de {origem} para {destino}")
        hanoi(qtde-1,aux,destino,origem)
print(hanoi(qtde=5,origem="A",destino="B",aux="C"))
print(mov)
