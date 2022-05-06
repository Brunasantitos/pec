def volver(c):
    cm = c.upper()
    return cm == "A" or cm == "E" or cm == "I" or cm == "O" or cm == "U"

def let(c):
    return "A" <= c.upper() <= "Z" and (not volver(c))

if __name__ == "__main__":
    letra = input().strip()
    print(let(letra))
