#Algoritmo de Eudclides
def mdc(x,y):
    if y ==0:
        return x
    else:
        return mdc(y,x%y)
print(mdc(x=120,y=200))