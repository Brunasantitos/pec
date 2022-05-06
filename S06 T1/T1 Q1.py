#função da definição do sexo 
nome = input().strip()
sexo = int(input().strip())
masculino = 1 
feminino = 2

#formação das coordenações

if sexo == masculino:
    print("Ilmo Sr.", nome)
else:
    print("Ilma Sra.", nome)
       
