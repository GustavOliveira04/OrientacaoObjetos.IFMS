def nested_sum(lista):
    soma = 0
    for sublista in lista:
        for elemento in sublista:
            soma += elemento
    return soma

# fora da função:

t = [[1, 2], [4, 4, 4], [5], [6, 6]]
nested_sum(t)
print(nested_sum(t))

#---------------------------------------------------

# def nested_sum(lista):
#     soma = 0

#     for sublista in lista:
#         for elemento in sublista:
#             soma += elemento
#     return soma
            
# # criar a lista fora da função

# t = [[1, 2], [4, 4, 4], [5], [6, 6]]
# nested_sum(t)
# print(nested_sum(t))
