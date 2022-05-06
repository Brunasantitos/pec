num1 = int(input().strip())
num2 = int(input().strip())
num3 = int(input().strip())
num4 = int(input().strip())
num5 = int(input().strip())
numero = num1
numero_1 = num1
if (num2 > numero): 
    numero = num2
if (num3 > numero): 
    numero = num3
if (num4 > numero): 
    numero = num4
if (num5 > numero): 
    numero = num5

if (num2 < numero_1): 
    numero_1 = num2
if (num3 < numero_1): 
    numero_1 = num3
if (num4 < numero_1): 
    numero_1 = num4
if (num5 < numero_1): 
    numero_1 = num5
print(numero)
print(numero_1)
