# DIP -  Dependency Inversion Principle (Princípio da Inversão de Dependência)

### 1. O que é? 
 - O princípio DIP é o último princípio do SOLID. Ele afirma que: 
     -  As classes principais (alto nível) que contêm regras de negócio não devem depender diretamente de classes auxiliares (baixo nível). Em vez disso, elas devem depender de uma interface que diz o que deve ser feito, sem se preocupar com o como.

### 2. Para que serve?
 - Reduzir o acoplamento entre classes.
 - Tornar o código mais flexível, testável e reutilizável.
 - Permitir a injeção de dependência, facilitando a troca de componentes sem alterar a lógica de negócio.

### 3. Explicação do código:
 - O código aplica o Princípio da Inversão de Dependência (DIP) separando a lógica principal da aplicação dos detalhes técnicos de como o e-mail é enviado. Em vez de depender diretamente de SmtpEmail, a classe Notificador recebe uma abstração chamada EnviadorEmail, que define o método enviar(). Isso permite que o Notificador funcione com qualquer classe que implemente essa abstração, sem precisar ser alterado.\ Explicação das Classes:

     - EnviadorEmail: é uma interface/abstração. Define o que deve ser feito (enviar()), mas não diz como.
     - SmtpEmail: é a implementação concreta que realmente sabe como enviar o e-mail via SMTP.
     - Notificador: é a classe principal (módulo de alto nível). Ela cuida da regra de negócio: enviar notificações.

### 4. Onde o SRP está sendo aplicado?
 - O DIP está sendo aplicado na classe Notificador, que depende de uma abstração (EnviadorEmail), e não de uma classe concreta como SmtpEmail. Assim, Notificador pode funcionar com qualquer tipo de envio, sem precisar ser alterado.

### 5. Quais problemas ele evita?
 - Evita forte acoplamento entre classes (as classes de regras de negócio não ficam presas a detalhes técnicos).
 - Permite fácil troca de implementação (você pode mudar a forma de envio sem mexer na lógica principal).
 - Ajuda nos testes unitários — você pode usar uma versão "falsa" (mock) da interface para testar a lógica do Notificador.
 - Deixa o sistema mais organizado, modular e escalável, separando claramente o que fazer (regra de negócio) de como fazer (implementação técnica).