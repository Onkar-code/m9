

"""
tupla = ('a', '1', '2', '-2', '+4', '5', 'sis')
resultat = [ valors for valors in tupla if not str(valors).isalpha()]   
parells = [ valors for valors in resultat if valors % 2 == 0 and valors > 0]
print(sum(parells))
"""
#~SOLUCIÓ 14
tupla = ('a', '1', '2', '-2', '+4', '5', 'sis')
lista_nomes_digits = [valors for valors in tupla if (valors[0] == '+' or valors[0] == '-' or valors.isdigit())]
#lista_parells = [int(valors) for valors in lista_nomes_digits if int(valors) % 2 == 0 and int(valors) > 0]
print(sum([int(valors) for valors in lista_nomes_digits if int(valors) % 2 == 0 and int(valors) > 0]))
#print(sum(list(map(int, parells))))

#~SOLUCIÓ 15
#tupla = ('a', '1', '2', '-2', '+4', '5', 'sis')
#lista_nomes_digits = [valors for valors in tupla if (valors[0] == '+' or valors[0] == '-' or valors.isdigit())]
print(sum(list(map(int, [valors for valors in tupla if (valors[0] == '+' or valors[0] == '-' or valors.isdigit())]))))
#print(sum(list(map(int, parells))))


#solució 16
print(tuple(map(int, lista_nomes_digits)))

#solució 17
def fins_un_maxim(tupla, maxim):
    """
    >>> fins_un_maxim((1, 7, 2, -2, 4, 2, 4), 7)
    (1, 1, 2, -2, 4)
    """
    resultado = 0
    #sumar hasta el valor máximo
    print([resultado for valors in tupla if (resultado = resultado + valors) < maxim])
    #tupla_2 = [resultado += valors for valors in tupla if resultado < maxim ]
    #print(tuple(map(int, tupla_2)))
    for valors in tupla:
        if resultado + valors <= maxim:
            tupla_2 = (valors, )
    print(tupla_2)        
            
    
