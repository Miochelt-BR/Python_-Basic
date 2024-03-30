"""""
Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. 
O objetivo é implementar três operações essenciais:
depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar 
suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.
"""""""""""

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
    
    def deposito(self, valor):
        if valor >= 0:
            self.saldo += valor
            print("Depósito de", valor, "realizado com sucesso.")
        else:
            print("Erro: O valor de depósito não pode ser negativo.")
    
    def saque(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print("Saque de", valor, "realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido. O valor deve ser maior que zero.")
    
    def extrato(self):
        print("Saldo atual:", self.saldo)


# Função principal para interação com o usuário
def main():
    conta = ContaBancaria()

    while True:
        print("\n===== Menu Principal =====")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                valor_deposito = float(input("Digite o valor a ser depositado: "))
                conta.deposito(valor_deposito)
            elif opcao == '2':
                valor_saque = float(input("Digite o valor a ser sacado: "))
                conta.saque(valor_saque)
            elif opcao == '3':
                conta.extrato()
            elif opcao == '4':
                print("Obrigado por utilizar nosso sistema bancário. Volte sempre!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico válido.")


# Chamada da função principal
if __name__ == "__main__":
    main()
