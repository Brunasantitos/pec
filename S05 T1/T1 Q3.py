#tempo de um evento
def evento(tempo):
    return hh,mm,ss
segundos = int(input())
hh = (segundos//3600)
mm = (segundos//60%60)
ss = segundos%60
print(f'{hh}:{mm}:{ss}')
