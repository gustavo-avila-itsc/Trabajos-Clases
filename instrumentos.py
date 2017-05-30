class Instrumentos():
    def __init__(self,tipo):
        self.tipo=tipo
    def sonar(self):
        print "sonando musica de", self.tipo
    def afinar(self):
        print "afinando instrumento"

class Guitarra(Instrumentos):
    def __init__(self,tipo,cuerda):

        Instrumentos.__init__(self,tipo)
        self.cuerda= cuerda
    def punteo(self):
        print "punteo"
class Piano(Instrumentos):
    def __init__(self,tipo,teclas):
        Instrumentos.__init__(self,tipo)
        self.teclas= teclas
    def concierto(self):
        print "sonando en concierto"
class Saxo(Instrumentos):
    
    def __init__(self, tipo,tamanio):
        Instrumentos.__init__(self,tipo)
        self.tamanio=tamanio
    def escala(self):
        print  self.tamanio
