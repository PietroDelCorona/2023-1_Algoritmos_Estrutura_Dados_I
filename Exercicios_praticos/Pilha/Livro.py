
class Livro:
    def __init__(self, titulo, autor, pg):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pg
        self.proximo = None

    def __str__(self):
        texto = "Título: " + self.titulo
        texto += "\nAutor: " + self.autor
        texto += "\nPáginas: " + str(self.pagina)
        return texto