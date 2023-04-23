import random
from datetime import datetime
import pytz
from random import randint

class Conta:
    """
    Cria um objeto Conta para gerenciar as contas dos clientes.

    Attributos:
    nome:(str) Nome do Cliente
    cpf:(str) Cpf do cliente. eve ser inserido com pontos e traços
    agencia: Agencia responsavel pela conta
    num_conta : Numero da conta do Cliente
    Saldo: Salddo disponivel na conta do cliente
    limite: Limite de cheque especial do cliente
    Transações: Transações de historico do cliente

    """



    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return  horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, 'Saldo: R${} '.format(self._saldo), Conta._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print("Você não tem saldo suficiente para sacar esse valor")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, 'Saldo: R${} '.format(self._saldo), Conta._data_hora()))

    def consultar_limite_chequeespecial(self):
        print("Seu limite de Cheque Especial é de R${:,.2f} ".format(self._limite_conta()))


    def historico_transacoes(self):
        print("Historico de Transações")
        print("Valor, Saldo, Data e Hora ")
        for transacao in self._transacoes :
            print(self._transacoes)


    def transferir (self,valor, conta_destino):
        self._saldo -=valor
        self._transacoes.append((-valor, 'Saldo: R${} '.format(self._saldo), Conta._data_hora()))
        conta_destino._saldo +=valor
        conta_destino._transacoes.append((valor, 'Saldo: R${} '.format(conta_destino._saldo), Conta._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self,titular, conta_corrente):
        self.numero = random.randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month,CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9), randint(0,9),randint(0,9))
        self.limite = 1000
        self._senha =  '1234'
        self.conta_correte = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self,valor):
        if len(valor) >=  4 and  valor.isnumeric():
            self._senha = valor
        else:
            print("Senha invalida")



