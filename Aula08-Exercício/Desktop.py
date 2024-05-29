from Produto import Produto


class Desktop(Produto): 
    def __init__(self, modelo, cor, preco, categoria , potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def cadastrar(self):
        print("Desktop cadastrado")
          
    def getInformacoes(self):
        return super().getInformacoes() +", \nPotência da Fonte: " + self._potenciaDaFonte

