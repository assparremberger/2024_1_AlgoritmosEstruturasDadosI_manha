from Produto import Produto


class Notebook(Produto): 
    def __init__(self, modelo, cor, preco, categoria , tempodebateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempodebateria
    
    def cadastrar(self):
        print("Notebook cadastrado")
        
    def getInformacoes(self):
        return super().getInformacoes() + f""", 
        Tempo de Bateria: {self.__tempoDeBateria}"""
    

