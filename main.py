from loja import *
from produto import *
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    loja = Loja()
    
    while True:
        limpar_tela()
        print("\n=== MENU ===")
        print("1. Adicionar produto ao estoque")
        print("2. Listar produtos")
        print("3. Adicionar ao carrinho")
        print("4. Visualizar carrinho")
        print("5. Remover do carrinho")
        print("6. Finalizar compra")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            limpar_tela()
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade em estoque: "))
            loja.adicionar_produto(Produto(nome, preco, quantidade))
            print("Produto adicionado com sucesso!")
            input("\nPressione Enter para continuar...")
        
        elif opcao == "2":
            limpar_tela()
            print("\n=== PRODUTOS ===")
            loja.listar_produtos()
            input("\nPressione Enter para continuar...")
        
        elif opcao == "3":
            limpar_tela()
            print("\n=== ADICIONAR AO CARRINHO ===")
            loja.listar_produtos()
            try:
                indice = int(input("\nNúmero do produto: "))
                quantidade = int(input("Quantidade: "))
                loja.adicionar_ao_carrinho(indice, quantidade)
            except:
                print("Entrada inválida!")
            input("\nPressione Enter para continuar...")
        
        elif opcao == "4":
            limpar_tela()
            print("\n=== VISUALIZAR CARRINHO ===")
            loja.visualizar_carrinho()
            input("\nPressione Enter para continuar...")
        
        elif opcao == "5":
            limpar_tela()
            print("\n=== REMOVER DO CARRINHO ===")
            loja.remover_do_carrinho()
            input("\nPressione Enter para continuar...")
        
        elif opcao == "6":
            limpar_tela()
            print("\n=== FINALIZAR COMPRA ===")
            loja.finalizar_compra()
            input("\nPressione Enter para continuar...")
        
        elif opcao == "7":
            print("\nSaindo do sistema...")
            break
        
        else:
            print("\nOpção inválida!")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
