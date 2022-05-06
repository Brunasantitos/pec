numero_1 = float(input().strip())
numero_2 = float(input().strip())
numero_3 = float(input().strip())
media = (numero_1 + numero_2 + numero_3) / 3
if numero_3 > 8:
    media = media + 1
if media > 10:
    media = 10
print(media)
    

