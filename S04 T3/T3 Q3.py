def valor(preco):
    return preco + pporcentagem
def valorDesconto(preco):
    return preco - pporcentagem
preco = float(input())
pporcentagem = float(input())
pporcentagem = pporcentagem*(preco/100)
print(f'{valor(preco):.2f}')
print(f'{valorDesconto(preco):.2f}')



