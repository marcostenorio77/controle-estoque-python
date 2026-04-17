# Sistema de Controle de Estoque para Madeireira

estoque = [] 

def adicionar_item():
    print("\n --- CADASTRO DE MADEIRAS ---")
    nome = input("Descrição do produto: ")

    try:
        qtd = int(input("Quantidade: "))
        preco = float(input("Preço Unitário R$: "))
    
        produto = {
            "nome": nome,
            "quantidade": qtd,
            "preco": preco,
            "valor_total": qtd * preco
        }
        
        estoque.append(produto)
        print("✅ Item adicionado ao estoque!")
    except ValueError:
        print("❌ Erro: No campo Quantidade e Preço, use apenas números.")
    
def gerar_relatorio():
    if not estoque:
        print("\nO estoque está vazio.")
        return

    print("\n" + "="*55)
    print(f"{'PRODUTO':<20} | {'QTD':<6} | {'PREÇO':<10} | {'TOTAL'}")
    print("-" * 55)

    total_financeiro = 0
    for item in estoque:
        # Acessando as chaves exatamente como foram criadas
        print(f"{item['nome']:<20} | {item['quantidade']:<6} | R${item['preco']:<8.2f} | R${item['valor_total']:.2f}")
        total_financeiro += item['valor_total']

    print("-" * 55)
    print(f"VALOR TOTAL DO ESTOQUE: R$ {total_financeiro:.2f}")
    print("="*55)

while True:
    print("\n MADEIREIRA - CONTROLE DE ESTOQUE")
    print("1. Cadastrar Produto")
    print("2. Ver Relatório Completo")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")
    match opcao:
        case "1":
            adicionar_item()
        case "2":
            gerar_relatorio()
        case "3":
            print("Saindo do sistema. Até logo!")
            break
        case _:
            print("Opção inválida. Tente novamente.")
















