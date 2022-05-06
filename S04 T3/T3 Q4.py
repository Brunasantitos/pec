def minutos(horas):
    x = horas//60
    y = horas%60
    return x,y

horas = int(input())
h,m = minutos(horas)
print(f'{h}:{m}') 

