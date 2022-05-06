dia = int(input().strip())
mes = int(input().strip())
ano = int(input().strip())
dia_1 = int(input().strip())
mes_2 = int(input().strip())
ano_3 = int(input().strip())

atual = ano - ano_3
if((mes < mes_2) or (dia < dia_1)): atual = atual - 1
elif(dia < dia_1): atual - atual - 1
print(atual)


    
    
    
    



