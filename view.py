from controller import VeiculoController

while True:
    decicao=int(input('''
    Digite ____ 1 .: para Cadastrar Veiculo
    Digite ____ 2 .: para Ler os Cadastros
    Digite ____ 3 .: para Sair do Programa
    '''))

    if decicao not in [1, 2, 3]:
        print('Opçao invalida tente novamente')
        continue
    elif decicao == 1:
        motor=float(input("Digite a potencia do motor? :"))
        porta=int(input("Digite a quantidade de porta? :"))
        cor=input("Qual a cor do veiculo? :")
        tanque=float(input("Quantos litros tem o tanque ? :"))
        if VeiculoController.cadastrar(motor, porta, cor , tanque):
            print("Cadastrado com sucesso")


    elif decicao == 2:
        print("Voce visualizou")
    elif decicao == 3:
        break