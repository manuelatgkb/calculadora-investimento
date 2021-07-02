import numpy as np
from datetime import datetime
import calculadora

dados = dict()
while True:
    dados['nome_do_anuncio'] = str(input('titulo do anúncio:  '))

    if len(dados['nome_do_anuncio'])<= 0:
        print("Tamanho mínimo de um caractere.")
        continue
    else:
        break
while True:
    dados['nome_do_cliente'] = str(input('Nome:  ' ))
    if len(dados['nome_do_cliente'])<= 0:
        print("Tamanho mínimo de um caractere.")
        continue
    else:
        break
while True:
    try:
        data_de_inicio = datetime.strptime(input('Data de início: '), '%d/%m/%Y')
    except ValueError:
        print("Favor inserir uma data no padrão dd/mm/yyyy.")
        continue
    else:
        break
while True:
    try:
        data_de_termino = datetime.strptime(input('Data de Término: '), '%d/%m/%Y')
        if (data_de_termino - data_de_inicio).days < 0:
            print('A data de término deve ser maior ou igual a data de início')
            continue
        else:
            break
    except ValueError:
        print("Favor inserir uma data no padrão dd/mm/yyyy.")
        continue
    else:
        break
periodototal = abs((data_de_termino - data_de_inicio).days)

dados['tempo de exposição restante em dias']  = data_de_termino - datetime.now()
while True:
    try:
        dados['investimentopordia'] = float(input('Investimento por dia em reais é de   : '))
        if dados['investimentopordia'] <= 0:
            print('O valor do investimeto deve ser maior que zero')
            continue
        else:
            calculadora.calcula(dados['investimentopordia'])
            break
    except ValueError:
        print("Somente valores numéricos são permitidos.")
        continue
    else:
        break
if dados['investimentopordia']!= 0:
    dados['Investtotal'] = dados['investimentopordia'] * periodototal


for k, v in dados.items():
    print(f' - {k} tem o valor de {v}')