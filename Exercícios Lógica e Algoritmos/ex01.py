
valor = int(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))
soma = valor * quantidade
if soma < 999:
    desconto = 0
elif soma >= 1000 and soma < 3000:
    desconto = (soma*3)/100
elif soma >= 3000 and soma < 5000:
    desconto = (soma*5)/100
else:
    desconto = (soma*8)/100

vcd = soma - desconto

print(f'O valor sem desconto é de {soma}')
print(f'O valor com desconto é de {vcd}')