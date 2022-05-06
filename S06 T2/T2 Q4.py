def isdigito(c):
    return '0' <= c <= '9'

def isletra(c):
    return "A" <= c.upper() <= "Z"

def showcaractere(c):
    return isletra(c) or isdigito(c)


if __name__ == "__main__":
    letra = input().strip()
    print(showcaractere(letra))
