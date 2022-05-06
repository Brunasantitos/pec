#projeto P3

print('''
Q1 - No Python, como se chama uma 'caixa' usada para armazenar dados?
a - texto
b - variavel
c - caixa de sapatos
''')
resposta = input().lower()
score = 0

if resposta == "a":
    print(" não - texto é um tipo de dado :( ")
elif resposta == "b":
    score = score + 1
    print(" correto! :) ", score)
elif resposta == "c":
    print(" não seja bobinho! :( ")
else:
     print(" você não escolheu a, b, c :( ")
    

print('''
Q2 - Qual o nome do primeiro computador criado?
a - enac
b - elsa
c - eniac
''')
resposta = input().lower()
if resposta == "a":
    print(" não :( ")
elif resposta == "b":
    print(" não :( ")
elif resposta == "c":
    score = score + 1
    print(" correto! :) S2 ", score)
else:
    print(" você não escolheu a, b, c :( ")

if score == 2:
    print ("muito bem")
else:
    print("tente novamente")


       
