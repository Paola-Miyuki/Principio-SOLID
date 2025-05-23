# codigo OCP

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CalculadoraPreco:
    def calcular(self, produto):
        return produto.preco

class CalculadoraPrecoComDesconto(CalculadoraPreco):
    def calcular(self, produto):
        return produto.preco * 0.9

# Exemplo de uso
produto_normal = Produto("Notebook", 3000)
produto_vip = Produto("Smartphone", 2000)

calculadora_normal = CalculadoraPreco()
calculadora_desconto = CalculadoraPrecoComDesconto()

print(f"Preço normal do {produto_normal.nome}: R${calculadora_normal.calcular(produto_normal)}")
print(f"Preço com desconto do {produto_vip.nome}: R${calculadora_desconto.calcular(produto_vip)}")
