from produto import Produto

class Loja:
    def __init__(self):
        self.produtos = [
            Produto("Carro", 3000, 7),
            Produto("Moto", 4000, 8),
            Produto("Navio", 5000, 9)
        ]
        self.carrinho = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def listar_produtos(self):
        for i, produto in enumerate(self.produtos, 1):
            print(f"{i}. {produto.nome} - R${produto.preco:.2f} ({produto.quantidade} disponíveis)")
    
    def adicionar_ao_carrinho(self, indice, quantidade):
        produto = self.produtos[indice-1]
        if produto.quantidade >= quantidade:
            self.carrinho.append((produto, quantidade))
            produto.quantidade -= quantidade
            print(f"{quantidade} {produto.nome}(s) adicionado(s) ao carrinho!")
        else:
            print("Quantidade indisponível!")
    
    def visualizar_carrinho(self):
        if not self.carrinho:
            print("\nCarrinho vazio!")
            return False
        
        print("\n=== SEU CARRINHO ===")
        total = 0
        for i, (produto, quantidade) in enumerate(self.carrinho, 1):
            subtotal = produto.preco * quantidade
            total += subtotal
            print(f"{i}. {quantidade}x {produto.nome} - R${produto.preco:.2f} cada = R${subtotal:.2f}")
        print(f"\nTOTAL: R${total:.2f}")
        return True
    
    def remover_do_carrinho(self):
        if not self.visualizar_carrinho():
            return
        
        try:
            indice = int(input("\nNúmero do item para remover: ")) - 1
            if indice < 0 or indice >= len(self.carrinho):
                print("Índice inválido!")
                return
            
            produto, qtd_atual = self.carrinho[indice]
            quantidade = int(input(f"Quantidade para remover (atual: {qtd_atual}): "))
            
            if quantidade <= 0:
                print("Quantidade deve ser positiva!")
            elif quantidade > qtd_atual:
                print("Não pode remover mais do que tem no carrinho!")
            else:
                produto.quantidade += quantidade
                if quantidade == qtd_atual:
                    self.carrinho.pop(indice)
                    print(f"Todos os {produto.nome} foram removidos do carrinho!")
                else:
                    self.carrinho[indice] = (produto, qtd_atual - quantidade)
                    print(f"{quantidade} {produto.nome}(s) removido(s) do carrinho!")
        except:
            print("Entrada inválida!")
    
    def finalizar_compra(self):
        total_original = sum(produto.preco * quantidade for produto, quantidade in self.carrinho)
        if total_original == 0:
            print("\nCarrinho vazio!")
            return
        
        self.visualizar_carrinho()
        print(f"\nTotal da compra: R${total_original:.2f}")
        
        forma = input("Forma de pagamento (cartao/pix/dinheiro): ").lower()
        cupom = input("Cupom de desconto (deixe em branco se não tiver): ")
        
        total_final = total_original
        desconto_total = 0
        
        if cupom == "des20":
            desconto_total += 20
            print(f"\nCupom 'des20' ativado (+20% de desconto)")
        elif cupom:
            print("\nCupom inválido - nenhum desconto adicional aplicado")
        
        if forma == "dinheiro" or forma == "pix":
            desconto_total += 10
            print(f"Pagamento com {forma.upper()} (+10% de desconto)")
        elif forma == "cartao":
            print("\nPagamentos no cartão não possuem desconto")
        else:
            print("\nForma de pagamento inválida - nenhum desconto aplicado")
        
        if desconto_total > 0:
            valor_desconto = total_original * (desconto_total / 100)
            total_final = total_original - valor_desconto
            print(f"\nDesconto total de {desconto_total}% aplicado!")
            print(f"Valor do desconto: R${valor_desconto:.2f}")
            print(f"Total com desconto: R${total_final:.2f}")
        else:
            print("\nNenhum desconto aplicado")
        
        total_pago = 0
        while total_pago < total_final:
            try:
                valor = float(input(f"\nValor a pagar (R${total_final - total_pago:.2f} restantes): R$"))
                if valor <= 0:
                    print("Valor deve ser positivo!")
                    continue
                
                total_pago += valor
                
                if total_pago < total_final:
                    print(f"Faltam R${total_final - total_pago:.2f}")
                else:
                    if total_pago > total_final:
                        print(f"Troco: R${total_pago - total_final:.2f}")
                    print("Pagamento concluído com sucesso!")
            except:
                print("Valor inválido! Digite um número.")
        
        self.carrinho = []
        print("\nCompra finalizada! Obrigado pela preferência.")