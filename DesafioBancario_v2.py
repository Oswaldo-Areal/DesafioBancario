"""# -*- coding: utf-8 -*-.

Created on Wed Sep  4 10:21:30 2024

@author:  Oswaldo Areal
"""


def sacar(*, saldo, valor, extrato, limite, numeros_saques, limite_saques):
    """Efetura saque."""
    if valor > saldo:
        print(f"Operação falhou. Teu saldo é de {saldo}.")
    elif numeros_saques == limite_saques:
        print(f"Operação falhou. Você já efetuou {(limite_saques)} saques.")
        print("Máximo permitido por dia.")
    elif valor > limite:
        print(f"Operação falhou. O valor limite de saque é de {limite}.")
    elif valor <= 0:
        print(f"Operação falhou. O valor do saque de {valor} \n.")
        print("é inválido. Deve ser maior que 0.")
    else:
        numeros_saques += 1
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    """Efetuar deposito."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Operação realizado com sucesso!\n")
    else:
        print(f"\n Erro! O {valor} é inválido.")

    return saldo, extrato


def mostrar_extrato(saldo, /, *, extrato):
    """Mostrar extrato."""
    print("\n########## Extrato ##########")
    print("Não foram realizadas movimentações."
          if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n#############################")


def criar_cliente(clientes):
    """Criar cliente do banco."""
    cpf = input("Digite o CPF (somente números são válidos): ")
    cliente = [cliente for cliente in clientes if cliente["cpf"] == cpf]

    if cliente:
        print(f"\n Já existe este CPF = {cpf}!")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço (rua, nº - bairro - cidade/estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento,
                     "cpf": cpf, "endereco": endereco})

    print("Operação realizada com sucesso!")


def criar_conta(agencia, numero, clientes):
    """Criar conta corrente do cliente do banco."""
    cpf = input("Informe o CPF do usuário: ")
    cliente = [cliente for cliente in clientes if cliente["cpf"] == cpf]

    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero,
                "usuario": cliente}

    print("\n Cliente não encontrado. Operação não pode ser realizada!")


def menu():
    """Apresentar o menu da aplicação bancária."""
    menu = """
    ******* MENU *******

    [D] Depositar
    [S] Sacar
    [E] Extrato
    [C] Nova conta
    [U] Novo cliente
    [Q] Sair
    Entre com a opção:
    ********************
    ==> """
    return input(menu)


if __name__ == "__main__":
    saldo = 0
    extrato = ""
    total_saques = 0
    LIMITE = 500
    LIMITES_SAQUES = 5
    AGENCIA = "00001"
    clientes = []
    contas = []
    while True:
        opcao = menu()
        if opcao.upper() == 'D':
            valor = float(input("Digite o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao.upper() == 'S':
            valor = float(input("Digite quanto deseja sacar: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato,
                                   limite=LIMITE, numeros_saques=total_saques,
                                   limite_saques=LIMITES_SAQUES)
        elif opcao.upper() == 'E':
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao.upper() == 'U':
            criar_cliente(clientes)
        elif opcao.upper() == 'C':
            criar_conta(AGENCIA, (len(contas) + 1), clientes)
        elif opcao.upper() == 'Q':
            print("Até logo!!!")
            break
        else:
            print(f"Opção {opcao} inválida.")
