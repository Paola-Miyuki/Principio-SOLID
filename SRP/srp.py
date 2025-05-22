#código srp


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class UsuarioRepositorio:
    def salvar(self, usuario):
        print(f"Salvando {usuario.nome} no banco de dados...")

class EmailServico:
    def enviar_email_boas_vindas(self, usuario):
        print(f"Enviando e-mail para {usuario.email}")
