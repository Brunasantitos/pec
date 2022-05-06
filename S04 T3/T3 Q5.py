def ordem(numero):
    a = numero%10
    numero = numero//10
    b = numero%10
    numero = numero//10
    c = numero%10
    numero = numero//10
    d = numero%10
    return a*1000 + b*100 + c*10 + d
numero = int(input())
print(ordem(numero))
    
