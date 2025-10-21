#correspondencia de 1 pra 1(indice)
cpf = []
saldo = []

def errocpf():
    print("Erro, este cpf não está registrado.")

def registro(): #armazenando dados do cliente
    cpf_user = str(input("cpf do cliente: "))
    cpf.append(cpf_user)
    print("cpf armazenado!")
    saldo_ini_user = float(input("saldo inicial do cliente: "))
    saldo.append(saldo_ini_user)
    print("saldo armazenado!")

def saque():
    cpf_user = str(input("digite o seu cpf: "))
    if cpf_user in cpf:
        valor_sacado = float(input("valor a ser sacado: "))
        conta = cpf.index(cpf_user)
        if saldo[conta] < 0:
            print("Erro, sua conta está negativada!")
        elif saldo[conta] < valor_sacado:
            print("Erro, o valor a ser sacado é maior do que o seu saldo.")
        else:
            saldo[conta] -= valor_sacado
            print(f"**********\nOperação concluída!\n**********")
            print(f"Você sacou {valor_sacado:.2f} reais! O seu saldo agora é {saldo[conta]:.2f}reais!\nTENHA UM BOM DIA!")
    else:
        errocpf()

def deposito():
    cpf_user = str(input("digite o seu cpf: "))
    if cpf_user in cpf:
        valor_depositado = float(input("valor a ser depositado: "))
        conta = cpf.index(cpf_user)
        saldo[conta] += valor_depositado
        print(f"**********\nOperação concluída!\n**********")
        print(f"Você depositou {valor_depositado:.2f} reais! O seu saldo agora é {saldo[conta]:.2f} reais!\nTENHA UM BOM DIA!")
    else:
        errocpf()

def transferencia():
    valor_operacao = float(input("valor a ser transferido: "))
    if len(cpf) >= 2:
        cpf_user = str(input("digite o seu cpf: "))
        cpf_transfer = str(input("digite o cpf do contemplado: "))
        if cpf_user and cpf_transfer in cpf:
            conta_user, conta_transfer = cpf.index(cpf_user), cpf.index(cpf_transfer)
            if valor_operacao > saldo[conta_user]:
                print("Erro, o valor a ser transferido é maior do que o seu saldo.")
            elif saldo[conta_user] < 0:
                print("Erro, sua conta está negativada!")
            else:
                saldo[conta_user] -= valor_operacao
                saldo[conta_transfer] += valor_operacao
                print(f"**********\nOperação concluída!\n**********")
                print(f"Você transferiu {valor_operacao:.2f} reais para o cpf {cpf_transfer}!\nO seu saldo agora é {saldo[conta_user]:.2f} reais!\nTENHA UM BOM DIA!")
        else:
            errocpf()

while True:
    entrada = str(input("deseja realizar alguma operação? ")) #registro, saque, deposito e transferencia
    if entrada == "registro":
        registro()
    elif entrada == "saque":
        saque()
    elif entrada == "deposito":
        deposito()
    elif entrada == "transferencia":
        transferencia()
    elif entrada == "não":
        break