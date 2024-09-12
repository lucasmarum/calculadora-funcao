print('''***************** Calculadora em python *****************
Selecione o número da operação desejada: 
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão ''')

esc = int(input('Digite sua opção: '))
n1 = float(input('Digite o primeiro número: '))
n2 = float(input("Digite o segundo número: "))


def soma (n1, n2):
    result = n1 + n2
    print(f'{n1} + {n2} = {result}')


def subtracao (n1, n2):
    result = n1 - n2
    print(f'{n1} - {n2} = {result}')


def multiplicacao (n1, n2):
    result = n1 * n2
    print(f'{n1} * {n2} = {result}')


def divisao (n1, n2):
    if n2 != 0:
        result = n1 / n2
        print(f'{n1} / {n2} = {result}')
    else:
        print('ERRO DIVISÃO POR 0')


if esc == 1:
    soma(n1,n2)

elif esc == 2:
    subtracao(n1, n2)

elif esc == 3:
    multiplicacao(n1, n2)

elif esc == 4:
    divisao(n1, n2)

else:
    print('Escolha invalida')