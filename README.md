# Lanchonete

A classe `Lanchonete` é uma implementação em Python para gerenciar os custos de produção de lanches em uma lanchonete.

## Métodos

### `__init__(self, precoIngredientes, lanches)`

O construtor da classe. Inicializa a lanchonete com os preços dos ingredientes e os lanches disponíveis. Calcula os custos de produção dos lanches.

### `consultaValorIngrediente(self)`

Imprime os valores dos ingredientes para cada mercado.

### `valorlanches(self)`

Calcula e imprime o valor dos lanches para cada mercado.

### `alterarValorIngredientes(self)`

Permite ao usuário alterar o valor de um ingrediente em um mercado específico.

### `custoProducao(self)`

Calcula o custo de produção de cada lanche para cada mercado, aplicando uma correção de 50%.

### `mostrarCustos(self)`

Imprime os custos de produção de cada lanche para cada mercado.

### `valoresNutricionais(self)`

Imprime os valores nutricionais dos ingredientes.

### `menu(self)`

Exibe um menu interativo para o usuário.

## Exemplo de uso

```python
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
