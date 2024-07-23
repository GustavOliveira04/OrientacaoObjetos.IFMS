def middle(lista):
    novalista = []

    for i, e in enumerate(lista):
        if i != 0 and i != len(lista) -1:
            novalista.append(e)

    return lista 

list = [1, 2, 3, 4]

listanova = middle(list)
print(listanova)