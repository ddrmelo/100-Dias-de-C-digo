num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print('-'*20)
print("""Menu de operações:
1 - Adição;
2 - Subtração;
3 - Multiplicação;
4 - Divisão""")
print('-'*20)
op = int(input("Qual operação deseja realizar? "))

if op == 1:
    tot = num1 + num2
    print(f'Adição: {num1} + {num2} = {tot}')

elif op == 2:
    tot = num1 - num2
    print(f'Subtração: {num1} - {num2} = {tot}')

elif op == 3:
    tot = num1 * num2
    print(f'Multiplicação: {num1} * {num2} = {tot}')
elif op == 4:
    tot = num1 / num2
    print(f'Divisão: {num1}/{num2} = {tot}')
else:
    print('Você digitou uma opção inválida!')