from abc import ABC, abstractmethod
from Categoria import Categoria

class Produto(ABC):
    def __init__(self,modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    @abstractmethod
    def cadastrar(self):
        pass

    def getInformacoes(self):
        texto = f"""Modelo: {self.modelo}, 
        Cor: {self.cor}, 
        Preço: {self.preco}, 
        Categoria: {self.categoria.nome}"""
        return texto

    