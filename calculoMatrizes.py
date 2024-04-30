class Lanchonete:
    def __init__(self, precoIngredientes, lanches):
        self.precoIngredientes = precoIngredientes
        self.lanches = lanches
        self.custos = self.custoProducao()

    def consultaValorIngrediente(self):
        for mercado, ingredientes in self.precoIngredientes.items():
            print(f"\nMercado '{mercado}'\nIngredientes:")
            for ingrediente, preco in ingredientes.items():
                print(f"- {ingrediente.capitalize()}: R${preco:.2f}")

    def valorlanches(self):
        for mercado, ingredientes in self.precoIngredientes.items():
            print(f"\nMercado: {mercado}\nIngredientes:")
            valor = 0
            for nome, ingrediente in self.lanches.items():
                print(nome)
                valor = (ingredientes['Pão'] * ingrediente['Pão']) + (ingredientes['Mortadela'] * ingrediente['Mortadela'])
                print(f"{valor:.2f}")

    def alterarValorIngredientes(self):
        print("[1] Pague Menos\n[2] Jaú Serve\n[3] Sair")
        mercado = int(input("Qual o mercado em que o ingrediente mudou de valor?\nOpção: "))
        match mercado:
            case 1:
                mercado = "Pague Menos"
            case 2:
                mercado = "Jaú Serve"
            case 3:
                return None
            case other:
                print("\nErro: Insira uma opção válida.\n")
                return None
        print("[1] Pão\n[2] Mortadela")
        ingrediente = int(input("Qual ingrediente deseja alterar?\nOpção: "))
        match ingrediente:
            case 1:
                ingrediente = "Pão"
            case 2:
                ingrediente = "Mortadela"
            case other:
                print("\nErro: Insira uma opção válida.\n")
                return None
        try:
            novo_valor = float(input("qual o novo valor?\nOpção: "))
        except (TypeError, ValueError):
            print("\nErro: Insira um valor válido.\n")
            pass
        except OverflowError:
            print("\nErro: O valor inserido é muito grande.\n")
            pass

        self.precoIngredientes[mercado][ingrediente] = novo_valor

    def custoProducao(self):
        custos = {}
        for mercado, ingredientes in self.precoIngredientes.items():
            custos[mercado] = {}
            for nome, receita in self.lanches.items():
                custo = sum(ingredientes[ingrediente] * quantidade for ingrediente, quantidade in receita.items())
                custo_corrigido = custo * 1.5  # Aplica a correção de 50%
                custos[mercado][nome] = custo_corrigido
        return custos

    def mostrarCustos(self):
        for mercado, custos_lanches in self.custos.items():
            print(f"\nMercado '{mercado}'\nCustos de produção (com correção de 50%):")
            for lanche, custo in custos_lanches.items():
                print(f"- {lanche}: R${custo:.2f}")

    def valoresNutricionais(self):
        # Valores nutricionais do Pão Francês (por 1kg)
        pao_frances = {
            "Calorias": 3000,  # kcal
            "Carboidratos": 586,  # g
            "Proteínas": 80,  # g
            "Gorduras": 31,  # g
            "Fibras": 23  # g
        }

        # Valores nutricionais da Mortadela (por 1kg)
        mortadela = {
            "Calorias": 2690,  # kcal
            "Carboidratos": 5.4,  # g
            "Proteínas": 110,  # g
            "Gorduras": 220,  # g
            "Fibras": 0  # g
        }

        print("Valores nutricionais por 1kg:")
        print("\nPão Francês:")
        for nutriente, valor in pao_frances.items():
            print(f"- {nutriente}: {valor}")

        print("\nMortadela:")
        for nutriente, valor in mortadela.items():
            print(f"- {nutriente}: {valor}")

    def menu(self):
        opcoes = [
            "=" * 80,
            "Seja bem-vindo à Lanchonete Chorume's".center(80),
            "-" * 80,
            "[1] Consultar valores dos ingredientes",
            "[2] Alterar preço dos ingredientes",
            "[3] valores dos lanches",
            "[4] Mostrar custo de produção",
            "[5] Valores nutricionais dos ingredientes",
            "[6] Sair",
            "=" * 80
        ]

        while True:
            for item in opcoes:
                print(item)

            try:
                menu = int(input("Opção: "))
            except (TypeError, ValueError):
                print("\nErro: Insira um número válido.\n")
                continue
            except OverflowError:
                print("\nErro: O valor inserido é muito grande.\n")
                continue

            match menu:
                case 1:
                    self.consultaValorIngrediente()
                case 2:
                    self.alterarValorIngredientes()
                case 3:
                    self.valorlanches()
                case 4:
                    self.mostrarCustos()
                case 5:
                    self.valoresNutricionais()
                case 6:
                    print("Saindo...")
                    break
                case other:
                    print("\nErro: Insira uma opção válida.\n")

if __name__ == "__main__":
    precoIngredientes = {
        "Pague Menos": {
            "Pão": 0.92,
            "Mortadela": 0.60
        },
        "Jaú Serve": {
            "Pão": 1.12,
            "Mortadela": 0.39
        }
    }

    lanches = {
        "Pão com Mortadela": {
            "Pão": 1,
            "Mortadela": 1
        },
        "Pão com mais Mortadela": {
            "Pão": 1,
            "Mortadela": 3
        }
    }

    lanchonete = Lanchonete(precoIngredientes, lanches)
    lanchonete.menu()
