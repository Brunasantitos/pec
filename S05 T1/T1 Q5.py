def pagamento_aVista(preco):
    return preco - (preco*9/100)

def pagamento_prestacao(preco):
    return preco / 5

def pagamento_10Vezes(preco):
    return (preco + (preco*17/100))/10

preco = float(input())

print(f'{pagamento_aVista(preco):.2f}')
print(f'{pagamento_prestacao(preco):.2f}')
print(f'{pagamento_10Vezes(preco):.2f}')



    
