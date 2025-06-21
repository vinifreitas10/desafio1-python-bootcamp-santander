menu = """

[d] Depósito
[s] Saque > limite de 3 saques diários no valor de 500
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True: 
    opcao = input(menu)

    if opcao == 'd':
        print("Depósito\n")
        deposito = float(input("Digite um valor: R$ "))
        if deposito < 0:
            print("Valor de depósito inválido!")
        else:
            saldo += deposito
            print(f"Depósito Realizado com Sucesso! seu saldo atual é de {saldo}")
            extrato += f"depósito: R$ {deposito}\n"
    elif opcao == 's':
        print("Saque\n")
        saque = float(input("Informe o valor que deseja sacar: R$ "))
        if saque > limite_por_saque:
            print("Não é possível sacar um valor maior do que R$ 500,00.")
        elif saque > saldo:
            print("Saldo insuficiente para realizar o saque!")
        else:
            print(f"Saque no valor de R${saque} realizado com sucesso!")
            saldo -= saque
            print(f"Saldo Atual: R$ {saldo}")
            extrato += f"saque: {saque}\n"
            numero_saques += 1
            if numero_saques == limite_saques:
                    print("limite diário de saques atingido!")
            
    elif opcao == 'e': 
        if extrato == "":
            print("Não foram realizadas movimentações!")
            print(f"saldo: {saldo}")       
        else:
            print("===============extrato===============\n")
            print(extrato)
            print(f"saldo: {saldo}")

    elif opcao == 'q':
        print("Desejamos um excelente dia!")
        break

    else:
        print("Operação inválida!")
