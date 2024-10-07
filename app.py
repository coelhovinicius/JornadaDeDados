# Transforma qualquer script Python em uma aplicação WEB
import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_no_postgres

def main():

    st.title("Sistema de CRM e Vendas - Frontend")
    email = st.text_input("Digite seu e-mail")
    data = st.date_input("Data da venda", datetime.now())
    hora = st.time_input("Hora da venda", value=time(9,0)) #Valor padrão: 9:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos vendidos", min_value=1, step=1)
    produto = st.selectbox("Produto Vendido", ["Gemini", "ChatGPT", "Llama3.0"])

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            
            #Verifica os dados informados e faz a validação do contrato
            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            
            st.write(venda)
            salvar_no_postgres(venda)
            
        except ValidationError as e:
            st.error(f"ERRO: {e}")

if __name__=="__main__":
    main()