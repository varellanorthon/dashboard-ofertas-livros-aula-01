"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros():
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Ocorreu algum erro na leitura do arquivo: ", error)
    
    return livros

def ler_livros_v2():
    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            print(arquivo.readline())
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Ocorreu algum erro na leitura do arquivo: ", error)


def ler_livros_v1():
    arquivo = None
    try:    
        arquivo = open("livros.csv", "r", encoding="utf-8")
        print(arquivo.readline())
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Ocorreu algum erro na leitura do arquivo: ", error)
    finally:
        if arquivo is not None:
            arquivo.close()

def calcular_preco_medio(livros):
    soma: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_Limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_original_Limpo)
        soma += preco_num
    
    media: float = soma/len(livros)
    return round(media, 2)

def contar_cinco_estrelas(livros):
    cont: int = 0
    for livro in livros:
        nota_limpa: str = livro["nota"].lower().strip()
        if(nota_limpa == "five"):
            cont = cont + 1
    
    return cont

def ler_livro_mais_caro(livros):
    preco_max: float = 0.0
    
    for livro in livros:
        preco_num = float(livro["preco"].replace("£", ""))
        if preco_max < preco_num:
            preco_max = preco_num
            nome_livro: str = livro["titulo"]
    
    return preco_max, nome_livro
        



if __name__ == "__main__":
    livros = ler_livros()
    print(f"A quantidade de livros da coleção é de {len(livros)}")
    preco_medio = calcular_preco_medio(livros)
    print(f"O preço médio é £{round(preco_medio,2)}")
    qntd_cinco_estrelas = contar_cinco_estrelas(livros)
    print(f"Quantidade de livros com cinco estrelas: {qntd_cinco_estrelas}")
    livro_mais_caro, nome_livro = ler_livro_mais_caro(livros)
    print(f"livro mais caro: {livro_mais_caro}")
    print(f"Titulo: {nome_livro}")