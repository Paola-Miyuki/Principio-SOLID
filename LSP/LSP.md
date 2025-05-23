# LSP- Liskov Substitution Principle (Princípio da Substituição de Liskov)

### 1. O que é?
- Se uma classe Filha herda de uma Classe Pai, devemos conseguir usar a filha no lugar da pai sem problemas, ou seja, subclasses devem manter o comportamento esperado da superclasse.

### 2. Para que serve? 
 - Evitar erros ao usar herança.
 - Garantir que a substituição de objetos por suas subclasses não quebre o sistema.
 - Manter a consistência e confiança ao usar polimorfismo.

### 3. Explicação do código
 - Esse código representa um sistema com aves. Temos: 
    - Uma classe base Ave com o método voar()

    - Duas subclasses: Andorinha e Pato, que herdam de Ave e implementam seu próprio comportamento de voo.

    - Uma função mostrar_voo() que aceita qualquer objeto do tipo Ave e chama o método voar(), exibindo o resultado.

