import csv
import dados

class livro:
    def __init__(self, titulo, preco, nota, categoria):
        self.titulo = titulo
        self.preco = preco
        self.nota = nota
        self.categoria = categoria

    def faixa(self):
        #converte a faixa de preço para caro, barato ou médio.
        if self.preco < 20:
            return "Barato"
        elif self.preco <=40:
            return "Medio"
        else:
            return "Caro"
    
    def estrelas(self):
        #converte nota para estrela: 3 -> "⭐⭐⭐".
        return "⭐" * self.nota

    def __str__(self):
        return f"{self.titulo} ($ {self.preco:2.f}"

'''
class favorito:
    def __init__(self, caminho, )
    #continuar outra hora#
'''
