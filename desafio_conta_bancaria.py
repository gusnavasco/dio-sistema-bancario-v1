import math

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_depositado = -1

        while valor_depositado < 0:
            valor_depositado = int(float(input("Quantia a ser depositada (número inteiro e positivo, digite 0 para cancelar): ")))
        if valor_depositado == 0:
            continue
        extrato += f"Depósito: R$ {valor_depositado}.00\n"
        saldo += valor_depositado

    elif opcao == "s":
        if numero_saques < 3:
            valor_sacado = -1
            
            while valor_sacado > 500 or valor_sacado < 0 or valor_sacado > saldo:
                valor_sacado = int(float(input("Quantia a ser sacada (número positivo menor ou igual a R$ 500.00 e ao saldo, digite 0 para cancelar): "))*100)/100
            if valor_sacado == 0:
                continue
            extrato += f"Saque: R$ {valor_sacado:.2f}\n"
            saldo -= valor_sacado
            numero_saques += 1

        else:
            print("O limite de saques diário já foi alcançado.")

    elif opcao == "e":
        print("--- Extrato ---")
        print(extrato)
        print(f"Saldo atual: {saldo:.2f}")
        input("\nPressione Enter para continuar")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")