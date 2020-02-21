# exercicio 1 - Dicionario - exiba o nome dos produtos com valor superior a R$50.00

produtos = {}

produtos['camiseta'] = 45.00
produtos['calça'] = 99.00
produtos['meia'] = 10.00
produtos['blusa'] = 55.00


print (produtos)

for k in produtos:
    if produtos[k] > 50.00:
        print(k,produtos[k])