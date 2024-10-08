import streamlit as st
import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
from contrato import Vendas

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para salvar os dados validados no PostgreSQL
def salvar_no_postgres(dados: Vendas):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()

        # Inserção dos dados na tabela "vendas"
        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados armazenados com sucesso no banco de dados")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")