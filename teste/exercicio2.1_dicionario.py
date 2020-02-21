# exercicio 1 - dicionario - com imput

produtos = {}     # usando o input 

for i in range(4):
    nome = input('produto:')
    preco = float(input('Preço:'))
    produtos[nome] = preco

'''
produtos[] = 
produtos[] = 
produtos[] = 
produtos[] = 

'''

print (produtos)

for k in produtos:                  #  exiba o nome dos produtos com valor superior a R$50.00
    if produtos[k] > 50.00:
        print(k,produtos[k])