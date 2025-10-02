import criacao_de_conta
def deposito(usuario):
    global saldo
    valor = float(input("valor a ser depositado: "))
    if valor < 0:
        print("operação inválida! o valor está negativo!")
    saldo += valor
    print(f"foi depositado {valor} reais, totalizando {saldo} reais de saldo!")
    return saldo

def saque(usuario):
    global saldo
    valor = float(input("valor a ser sacado: "))
    if valor > saldo:
        print("operação inválida! o valor requerido supera o saldo disponível")
        pass
    else:
        saldo -= valor
        print(f"foi sacado {valor} reais, restando {saldo} reais de saldo!")
    return saldo

def status(usuario):
    global saldo
    pergunta = str(input("gostaria de saber o saldo atual? S/N"))
    if pergunta == "S":
        print(saldo)
    else:
        pass
    return saldo

def verificacao(usuario, saldo):
    criacao_de_conta.banco_de_usuarios
    if usuario in banco_de_usu