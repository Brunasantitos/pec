def volver(c):
    return "A" <= c.upper() <= "Z"

if __name__ == "__main__":
    letra = input().strip()
    print(volver(letra))
