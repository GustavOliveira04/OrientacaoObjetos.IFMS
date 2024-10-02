def juntar_dicionario(dict1, dict2):
    dict = dict1.copy()
    dict.update(dict2)
    return dict

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
 
resultado = juntar_dicionario(dict1, dict2)
print(resultado) 


#--------------------------------------------------------------------
# outra resolução:

# def merge(d1, d2):
#     dict = {}
#     for e in d1:
#         dict[e] = d1[e]
#     for e in d2:
#         dict[e] = d2[e]
#     return dict


# x = {'dez': 10, 'vinte': 20, 'trinta': 30}
# y = {'trinta': 30, 'quarenta': 40}
# mesclado = merge(x, y)
# print(mesclado)

#--------------------------------------------------------------------
# de outra forma:

# def merge(d1, d2):
#     return d1 | d2

# x = {'dez': 10, 'vinte': 20, 'trinta': 30}
# y = {'trinta': 30, 'quarenta': 40}
# mesclado = merge(x, y)
# print(mesclado)
