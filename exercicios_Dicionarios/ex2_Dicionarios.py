def juntar_dicionario(dict1, dict2):
    dict = dict1.copy()
    dict.update(dict2)
    return dict

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

resultado = juntar_dicionario(dict1, dict2)
print(resultado) 


#--------------------------------------------------------------------
# resolvendo de outra maneira:

# def juntar_dicionarios(dict1, dict2):
#     resultado = {}

#     for chave, valor in dict1.items():
#         resultado[chave] = valor
    
#     for chave, valor in dict2.items():
#         resultado[chave] = valor

#     return resultado

# # Teste

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# resultado = juntar_dicionarios(dict1, dict2)
# print(resultado)