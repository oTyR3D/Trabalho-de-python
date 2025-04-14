class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def atualizar_estoque(self, quantidade_vendida):
        self.quantidade += quantidade_vendida