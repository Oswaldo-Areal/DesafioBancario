"""# -*- coding: utf-8 -*-.

Created on Mon Sep  2 11:33:43 2024

@author: Oswaldo Areal
"""


def sacar(saques, saldo, extrato):
    """Efetura saque."""
    LIMITE_SAQUE = 500
    LIMITE_DE_SAQUES = 3

    valor = float(input("Informe o valor do saque: "))
    if valor > saldo:
        print(f"Operação falhou. Teu saldo é de {saldo}.")
    elif saques == LIMITE_DE_SAQUES:
        print(f"Operação falhou. Você já efetuou {(LIMITE_DE_SAQUES)} saques.")
        print("Máximo permitido por dia.")
    elif valor > LIMITE_SAQUE:
        print(f"Operação falhou. O valor limite de saque é de {LIMITE_SAQUE}.")
    elif valor <= 0:
        print(f"Operação falhou. O valor do saque de {valor} \n.")
        print("é inválido. Deve ser maior que 0.")
    else:
        saques += 1
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
    return saques, saldo, extrato


def depositar(saldo, extrato):
    """Efetuar deposito."""
    valor = float(input("Informe o valor do depósito: "))
    if valor <= 0:
        print(f"Operação falhou. Valor de {valor} é inválido.")
        return saldo, extrato
    extrato += f"Depósito: R$ {valor:.2f}\n"
    saldo += valor
    return saldo, extrato


def mostrar_extrato(extrato):
    """Mostrar extrato."""
    print("\n########## Extrato ##########")
    print("Não foram realizadas movimentações."
          if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n#############################")

menu = """
       *** MENU ***

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

       ************
"""

saldo = 0

saques = 0
extrato = ""


while True:
    opcao = input(menu)

    if opcao.upper() == 'D':
        saldo, extrato = depositar(saldo, extrato)

    elif opcao.upper() == 'S':
        saques, saldo, extrato = sacar(saques, saldo, extrato)

    elif opcao.upper() == 'E':
        mostrar_extrato(extrato)

    elif opcao.upper() == 'Q':
        break

    else:
        print(f"Opção {opcao} inválida. Digite D / S / E / Q.")
