
def escolha_servico():
    while True:
        serviço = str(input('''(DIG) - Digitalização\n(ICO) - Impressão Colorida\n(IBO) - Impressão Preto e Branco\n(FOT) - Fotocópia 
Entre com o tipo de serviço desejado: ''')).strip().upper()
        if serviço == 'DIG':
            valor = 1.10
        elif serviço == 'ICO':
            valor = 1
        elif serviço == 'IBO':
            valor = 0.4
        elif serviço == 'FOT':
            valor = 0.2
        else:
            print('Tipo de serviço inválido')
            continue
        break
    return valor

def num_paginas():
    while True:
        try:
            numpag = int(input('Entre com o número de páginas: '))
            if numpag < 10:
                desconto = 0
            elif 10 <= numpag < 100:
                desconto = 1.0
            elif 100 <= numpag < 1000:
                desconto = 0.85
            elif numpag >= 1000:
                desconto = 0.8
            else:
                raise ValueError('Valor maior que 1000 ou não numérico')
            numpag_desconto = int(numpag * desconto)
            return numpag_desconto
        except ValueError as e:
           print(f'ERRO: {e}')

def servico_extra():
    while True:
        try:
            adicional = int(input('''Qual serviço adicional deseja?\nEncardenação simples(1)\nEncardenação de capa dura(2)\nNão quer mais nada(0): '''))
            if adicional == 1:
                extra = 10
            elif adicional == 2:
                extra = 25
            elif adicional == 0:
                extra = 0
            else:
                raise ValueError('Valor digitado diferente de 1, 2 ou 0')
            return extra
        except ValueError as x:
            print(f'ERRO: {x}')


resultado=escolha_servico()
desc=num_paginas()
valor_extra=servico_extra()
total = resultado * desc + valor_extra
print(f'O total a ser pago é de {total}')