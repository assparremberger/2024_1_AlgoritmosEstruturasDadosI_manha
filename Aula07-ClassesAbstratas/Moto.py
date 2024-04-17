from Veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, modelo, ano, cilindradas):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas

    def ligar(self, chave):
        if chave == "1234" :
            print("Motocicleta Ligada")
        else:
            print( "Não foi possível ligar a Motocicleta")

    def imprimir(self):
        print( "Motocicleta: ")
        super().imprimir()
        print( "Cilindradas: " , self.cilindradas)