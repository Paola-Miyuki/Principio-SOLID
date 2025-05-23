# SRP — Single Responsibility Principle (Princípio da Responsabilidade Única)

### 1. O que é? 
 - Uma classe deve ter apenas uma única responsabilidade. Isso significa que ela deve fazer apenas uma coisa, e ter um único motivo para mudar.

### 2. Para que serve?
 - Evita que uma mesma classe tenha várias funções diferentes, o que dificulta a manutenção, os testes e a organização do sistema.

### 3. Explicação do código:
 - Esse sistema simula um processo simples de cadastro de usuário com envio de e-mail de boas-vindas. Ele está dividido em três responsabilidades separadas, cada uma com sua própria classe:
     * Usuario → apenas representa os dados do usuário.
     * UsuarioRepositorio → salva o usuário no banco (simulado com um print).
     * UsuarioEmailService → envia o e-mail de boas-vindas (também simulado).

### 4. Onde o SRP está sendo aplicado?
 - Cada classe faz apenas uma tarefa específica. Se a forma de salvar no banco ou de enviar e-mail mudar, somente uma classe será alterada, sem afetar as demais.

### 5. Quais problemas ele evita?
 - Facilita manutenção, testes e evita que uma única classe fique cheia de responsabilidades diferentes.