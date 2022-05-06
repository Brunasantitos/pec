def digito(c):
    return '0' <= c <= '9'

def volver(c):
    cm = c.upper()
    return cm == "A" or cm == "E" or cm =="I" or cm =="O" or cm =="U" 

def isletra(c):
    return "A" <= c.upper() <= "Z"

def consoante(c):
    return (not (volver(c))) and isletra(c)



if __name__ == '__main__':
    letra = input()
    if volver(letra): print("vogal")
    elif consoante(letra): print("consoante")
    elif digito(letra): print("número")
    elif (not isletra(letra)) and (not digito(letra)) : print("símbolo")
