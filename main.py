from ContasBancos import Conta, CartaoCredito
#programa
conta_gabriel = Conta("Gabriel", "22222", 1234 , 43298)

cartao_gabriel = CartaoCredito('gabriel', conta_gabriel)
print(cartao_gabriel.titular)
print(cartao_gabriel.numero)
print(cartao_gabriel.validade)
print(cartao_gabriel.cod_seguranca)
print(cartao_gabriel.conta_correte)

print('---' * 30)

cartao_gabriel.senha  = '12345'
print(cartao_gabriel.senha)