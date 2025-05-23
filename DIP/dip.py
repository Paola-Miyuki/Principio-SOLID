#cod dip

# Abstração
class EnviadorEmail:
    def enviar(self, destinatario, mensagem):
        raise NotImplementedError("Método abstrato.")

# Implementação concreta
class SmtpEmail(EnviadorEmail):
    def enviar(self, destinatario, mensagem):
        print(f"Enviando e-mail via SMTP para {destinatario}: {mensagem}")

# Módulo de alto nível
class Notificador:
    def __init__(self, enviador: EnviadorEmail):
        self.enviador = enviador

    def notificar_usuario(self, usuario_email, mensagem):
        self.enviador.enviar(usuario_email, mensagem)

# Uso
email_smtp = SmtpEmail()
notificador = Notificador(email_smtp)
notificador.notificar_usuario("paolamiyuki@email.com", "Bem-vinda ao sistema!")
