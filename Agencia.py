from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []


    def vericar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado, Caixa Atual: R${:,.2f} '.format(self.caixa))
        else:
            print('O valor de caixa está OK. Caixa Atual :  R${:,.2f} '.format(self.caixa))

    def emprestar_dinheiro(self,valor,cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor,cpf,juros))
            print('Emprestimo feito com sucesso o valor de R${} já está na sua conta'.format(valor))

        else:
            print("Emprestimo não é possivel. Dinheiro não disponivel em caixa.")


    def adicionar_cliente(self,nome,cpf,patrimonio):
        self.clientes.append((nome,cpf,patrimonio))
        print('Bem vindo a nossa Agencia senhor {}'.format(nome))


class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0


    def depositar_paypal(self,valor):
        self.caixa -= valor
        self.caixa_paypal += valor
        print('Parabéns o deposito do {}, foi efetuado com Sucesso'.format(valor))

    def sacar_paypal(self,valor):
        self.caixa_paypal -=valor
        self.caixa += valor
        print('Parabéns o saque no {}, foi efetuado com Sucesso'.format(valor))




class AgenciaComum(Agencia):
    def __init__(self,telefone,cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 10000000


class AgenciaPremium(Agencia):
    def __init__(self,telefone,cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 100000000


    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
            print('Welcome to the Agencia premium')
        else:
            print("O cliente não tem patrimônio necessario para entrar na agencia premium")





agencia1 = Agencia(321312312,20000000,1234)

agencia1.caixa = 1000000
agencia1.vericar_caixa()
print('---' *30)

agencia1.emprestar_dinheiro(1500,2312312,0.02)
print('---' *30)

agencia1.adicionar_cliente('Gabriel Oliveira', 12345678910,10000)
print('---' * 30)
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br',2222,3424234)
print(agencia_virtual.vericar_caixa())
print('---' * 30)
agencia_virtual.depositar_paypal(50000)
print('---' * 30)
agencia_virtual.sacar_paypal(10000)
print('---' * 30)

agencia_premium = AgenciaPremium(2222333333,4234234234)
agencia_premium.adicionar_cliente('Gabriel',32123123,10000000 )

