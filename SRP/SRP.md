SRP — Single Responsibility Principle (Princípio da Responsabilidade Única)
-  O que é?
Uma classe deve ter apenas uma única responsabilidade. Isso significa que ela deve fazer apenas uma coisa, e ter um único motivo para mudar.

-  Para que serve?
Evita que uma mesma classe tenha várias funções diferentes, o que dificulta a manutenção, os testes e a organização do sistema.

Explicação do código:
* A classe Usuario só representa o usuário.
* A classe UsuarioRepositorio é responsável apenas por salvar usuários no banco de dados.
* A classe EmailServico cuida apenas do envio de e-mails.

-> Onde o SRP está sendo aplicado:
Cada classe faz apenas uma tarefa específica. Se a forma de salvar no banco ou de enviar e-mail mudar, somente uma classe será alterada, sem afetar as demais.

-> Quais problemas ele evita?
Facilita manutenção, testes e evita que uma única classe fique cheia de responsabilidades diferentes.