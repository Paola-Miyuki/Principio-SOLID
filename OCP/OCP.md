OCP — Open-Closed Principle (Princípio Aberto-Fechado)

-> O que é? 
* As classes devem estar abertas para extensão, mas fechadas para modificação. Ou seja, podemos adicionar comportamentos novos sem precisar mudar o código antigo.

-> Explicação do código:
-  Este código simula um sistema simples de cálculo de preços para produtos, onde:Um produto tem nome e preço, e existe uma classe que calcula o preço normal e existe outra classe que calcula o preço com desconto de 10%.

* A classe Produto armazena o preço.
* CalculadoraPreco é uma classe genérica para calcular o preço.
* CalculadoraPrecoVIP é uma classe que estende a base para aplicar um desconto.

-> Onde o OCP está sendo aplicado?
* A classe CalculadoraPreco é fechada para modificação. Não precisamos mudar ela se quisermos aplicar um desconto.
* Em vez disso, criamos uma nova classe CalculadoraPrecoComDesconto que estende (herda) a original e adiciona um novo comportamento
* Assim, o sistema está aberto para extensão sem alterar a classe existente.


-> Quais problemas ele evita?
- Evitamos alterar o código antigo, o que reduz riscos de bugs e facilita a manutenção e evolução do sistema.


