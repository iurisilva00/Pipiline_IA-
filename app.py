import streamlit as st
from datetime import datetime,time
from contrato import Vendas 
from pydantic import ValidationError
from database import salvar_no_postgres
def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email=st.text_input("Campo de texto para inserção do email do vendedor")
    data=st.date_input("Iserir Data")
    hora=st.time_input("Inserir Hora")
    valor = st.number_input("Valor da venda",min_value=0.0, format="%.2f")
    
    quantidade=st.number_input("Campo para inserir a quantidade de produtos vendidos")
    produto=st.selectbox("Campo para escolher o produto vendido",["Zapflow com Gemini","Zapflow com ChatGpt","Zapflow com Llama"])
    
    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data,hora)
            venda=Vendas(
                email =email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto
            )
            st.write(venda)
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")
        # st.write("**Dados da Venda:**")
        # st.write(f"Email do Vendedor:{email}")
        # st.write(f"Data e hora da Compra:{data_hora}")
        # st.write(f"Valor da Venda: R${valor:.2f}")
        # st.write(f"Quantidade de Produtos: {quantidade}")
        # st.write(f"Produto: {produto}")
if __name__ == "__main__":
    main()
