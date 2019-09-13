import sys

try:
    numero = int(sys.argv[1])
    operacao = sys.argv[2]
except:
    numero = False
    operacao = False




def soma():
    contador = 0
    print('SOMA')
    while contador <= 9:
        soma = numero + contador
        print("{} + {} = {}".format(numero, contador, soma))
        contador+=1

def subtracao():
    contador = 0
    while contador <= 9:
        subtracao = numero - contador
        print("{} - {} = {}".format(numero, contador, subtracao))
        contador+=1

def multiplicacao():
    contador = 0
    while contador <= 9:
        multiplicacao = numero * contador
        print("{} x {} = {}".format(numero, contador, multiplicacao))
        contador+=1

def divisao():
    contador = 1
    while contador <= 9:
        divisao = numero / contador
        print("{} / {} = {:.2f}".format(numero, contador, divisao))
        contador+=1



if operacao == 'som':
    soma()
elif operacao == 'sub': 
    subtracao()
elif operacao == 'mult':
    multiplicacao()
elif operacao == 'div':
    divisao()
else:
    print('tabuada.py [numero] [operação]')
    print("""
    som = soma
    sub = subtração
    mult = multiplicação
    div = divisão
    """)

    