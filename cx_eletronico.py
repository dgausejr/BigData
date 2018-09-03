# Programa cx_eletronico.py
# Dionisio Gause Junior - 02/09/2018

print('Caixa Eletrônico - Projeto Big Data\n')

v1 = float(input('Quanto você deseja sacar? R$ '))
vtotal = v1
cedula = 100
qtdced = 0
minimo = 5
maximo = 2000

while True:

    # primeiro teste se valor está dentro do periodo proposto
    # entre o mínimo e o máximo

    if v1 < minimo:
        print(f'O valor esta abaixo do mínimo - R$ {minimo:.2f}')
        break
    elif v1 > maximo:
        print(f'O valor esta acima do máximo - R$ {maximo:.2f}')
        break
    else:

        if vtotal >= cedula:
            vtotal -= cedula
            qtdced += 1
        else:
            if qtdced > 0:
                print(f'você receberá {qtdced} cédulas de R$ {cedula:.2f}')
            if cedula == 100:
                cedula = 50
            elif cedula == 50:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 1
            qtdced = 0
            if vtotal == 0:
                break
