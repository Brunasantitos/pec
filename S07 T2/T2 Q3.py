def Par(num):
    return num % 2 == 0


def DoisDigitos(num):
    return num > 9 and num < 100


if __name__ == "__main__":
    num = int(input().strip())
    #78
    d1 = (num//10) #78/10= 8
    d2 = num % 10 #78 % 10 = 8
        
    if (DoisDigitos(num) and Par(d1) and Par(d2)): 
        print("Nenhum dígito é ímpar.")
    elif (DoisDigitos(num) and ((not Par(d1) and Par(d2))or(not Par(d2) and Par(d1)))): 
        print("Apenas um dígito é ímpar.")
    elif (DoisDigitos(num) and (not Par(d1) and not Par(d2))): 
        print("Os dois dígitos são ímpares.")
