def desvioPadraoAmostral (lista):
    elementos = len(lista)
    media = sum(i for i in range(5))/elementos
    
    topTotal = 0

    for i in lista: 
        soma = (i - media)**2
        topTotal += soma

    desvio = topTotal / elementos - 1
    return desvio 

def desvioTotal (lista):
    elementos = len(lista)
    media = sum(i for i in range(5))/elementos
    
    topTotal = 0

    for i in lista: 
        soma = (i - media)**2
        topTotal += soma

    desvio = topTotal / elementos
    return desvio 

l = [10,20,12,17,16]

print(desvioPadraoAmostral(l))
print(desvioTotal(l))
