saldo = 5000
valor_saque = 1 

print(f'seu saldo e {saldo}')

while valor_saque != 0:
    valor_saque = float(input('informe o valor do saque '))
    saldo -=saldo - valor_saque
    print(f'seu saldo e {saldo}')