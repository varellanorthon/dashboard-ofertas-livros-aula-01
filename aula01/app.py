"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

# Configs da pagina
st.set_page_config(layout = "wide")
st.title("📚 Dashboard de Livros")
st.write("Se você está vendo esta página, o seu ambiente está pronto! 🎉")
col1, col2, col3, col4 = st.columns(4)

# Calculo dos dados
livros = dados.ler_livros()
qntd_livros = len(livros)
preco_medio = dados.calcular_preco_medio(livros)
qntd_livros_cinco_estrelas = dados.contar_cinco_estrelas(livros)
livro_mais_caro, nome_mais_caro = dados.ler_livro_mais_caro(livros)

# Display dos dados
col1.metric("Total de livros", qntd_livros)
col2.metric("Preço médio: ", f"£{preco_medio}")
col3.metric("Quantidade de livros com cinco estrelas ", qntd_livros_cinco_estrelas)
col4.metric("Livro mais caro ", f"£{livro_mais_caro}")
col4.metric("Título: ", nome_mais_caro)
st.dataframe(livros)
