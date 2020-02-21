def intercala(tupla1, tupla2):
    tupla3 = ()
    
    for i in range(len(tupla1)):
        tupla3 = tupla3 + (tupla1[i],) + (tupla2[i],)
    
    return tupla3
