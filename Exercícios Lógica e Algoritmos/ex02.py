acumulador = 0
print('BEM VINDO')
print(''' ------------------ Cardápio ----------------------
 -----| Tamanho |  Cupuaçu (CP) |  Açaí (AC) |-----
 -----|    P    |  R$ 10,00     |   R$ 12,00 |-----
 -----|    M    |  R$ 15,00     |   R$ 17,00 |-----
 -----|    G    |  R$ 19,00     |   R$ 21,00 |----- ''')
print('-' * 52)
while True:
    sabor = str(input('Sabor desejado: ')).strip().upper()
    if sabor not in "CP,AC":
        print('Sabor inválido, tente novamente')
        continue
    while True:
            tamanho = str(input('Tamanho desejado: ')).strip().upper()
            if tamanho not in 'PMG':
                print('Tamanho inválido, tente novamente')
                continue

            if sabor == 'CP':
                if tamanho == 'P':
                    valor = 10
                elif tamanho == 'M':
                    valor = 15
                else:
                    valor = 19
            else:
                if sabor == 'AC':
                    if tamanho == 'P':
                        valor = 12
                    elif tamanho == 'M':
                        valor = 17
                    else:
                        valor = 21

            acumulador += valor
            break
    mais = str(input('Deseja pedir mais alguma coisa?')).strip().upper()
    if mais != 'S':
        break
print(f'O total a ser pago é {acumulador:.2f}')

