from model import Veiculo

class VeiculoDal:
    @classmethod
    def salvar(cls, veiculo:Veiculo):
        with open('Carros.txt','a') as arq:
            arq.writelines(str(veiculo.motor) + " " + str(veiculo.porta) + " " + veiculo.cor + " " + str(veiculo.tanque) + "\n" + "\n")

    @classmethod
    def ler(cls):
        pass