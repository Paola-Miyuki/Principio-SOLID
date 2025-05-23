#cod de lsp


class Ave:
    def voar(self):
        return "Esta ave está voando."

class Andorinha(Ave):
    def voar(self):
        return "A andorinha está voando rápido."

class Pato(Ave):
    def voar(self):
        return "O pato está voando baixo."


def mostrar_voo(ave: Ave):
    print(ave.voar())

andorinha = Andorinha()
pato = Pato()

mostrar_voo(andorinha)  
mostrar_voo(pato)      
