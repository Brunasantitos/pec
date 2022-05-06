def Par(num):
    return num % 2 == 0


if __name__ == "__main__":
    num = int(input().strip())
    pares = 0
    d1 = num//100
    d2 = (num//10) % 10
    d3 = num % 10
    if (Par(d1) and d1 > 0):
        pares = pares + 1
    if (Par(d2)):
        pares = pares + 1
    if (Par(d3)):
        pares = pares + 1
    print(pares)

