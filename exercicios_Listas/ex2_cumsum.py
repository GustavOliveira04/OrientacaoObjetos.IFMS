def cumsum(lista):
    novalista = []

    for indice, elemento in enumerate(lista):
        soma = 0
        for j  in range(indice):
            soma += lista[j]
        novalista.append(soma + elemento)
    return novalista 

# fora da função:

t = [3, 1, 5, 4]
print(cumsum(t))

#---------------------------------------------------------

# def cumsum(lista):
#     novalista = []

#     for indice, elemento in enumerate(lista):
#         soma = 0
#         for j in range(indice):
#             soma += lista[j]
#         novalista.append(soma + elemento)
#     return novalista
