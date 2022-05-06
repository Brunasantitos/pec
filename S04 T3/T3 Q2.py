def areaQuadrado(lado):
    return lado * lado


def perimetroQuadrado(p):
    return p*4


lado = float(input().strip())
print(f'{areaQuadrado(lado):10.4f}')
print(f'{perimetroQuadrado(lado):10.4f}')

    
