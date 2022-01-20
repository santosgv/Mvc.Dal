from dal import VeiculoDal
from model import Veiculo

class VeiculoController:
    @classmethod
    def cadastrar(cls, motor, porta, cor, tanque):

        try:
            if (motor > 0) and (porta >= 2):
                VeiculoDal.salvar(Veiculo(motor, porta, cor, tanque))
                return True

            elif motor < 0:
                print('O motor Precisa ser maior que 0')
                return False

            elif porta < 2:
                print('A porta e menor que 2')
                return False

            elif tanque < 5.0 :
                print('O tanque nao pode ser menor que 5')
                return False
            else:
                print('Erro interno')
                return False

        except Exception as E:
            print(E)
            return False
