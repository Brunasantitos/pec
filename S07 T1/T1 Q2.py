dia = int(input())
mes = int(input())
ano = int(input())
di = int(input())
me = int(input())
an = int(input())

if dia >= di and mes >= me and ano >= an:
    print(f'{dia}/{mes}/{ano}')
else:
    print(f'{di}/{me}/{an}')
