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
        print("\n================ DEPÓSITO ================")
        valor_str = input("Informe o valor do depósito: ")   
        if valor_str.isdigit():
            # Convertendo a string para float
            valor = float(valor_str)
            if valor > 0:
                saldo += valor
                extrato += f"Depósito de R$ {valor:.2f}\n"

            else:
                print("Valor inválido para depósito.\n")
        else:
            print("Entrada inválida. Por favor, insira um número.\n")

    elif opcao == "s":
        print("\n================ SAQUE ===================")
        valor_str = input("Informe o valor do saque: ")
        if valor_str.isdigit():
            valor = float(valor_str)
            if valor > saldo:
                print("Saldo insuficiente para saque.\n")
            elif valor > limite:
                print(f"Valor do saque excede o limite de R$ {limite:.2f}.\n")
            elif numero_saques >= LIMITE_SAQUES:
                print(f"Limite de saques diários atingido ({LIMITE_SAQUES} saques).\n")
            else:
                saldo -= valor
                extrato += f"Saque de R$ {valor:.2f}\n"
                numero_saques += 1
                

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato:
            print(extrato)
            
        else:
            print("Nenhum movimento realizado.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print('\n=========================================')
        
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
