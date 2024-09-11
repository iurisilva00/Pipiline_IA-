import streamlit as st
from datetime import datetime,time
import contrato
def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")
    email=st.text_input("Campo de texto para inserção do email do vendedor")
    data=st.date_input("Iserir Data")
    hora=st.time_input("Inserir Hora")
    valor = st.number_input("Valor da venda",min_value=0.0, format="%.2f")
    
    quantidade=st.number_input("Campo para inserir a quantidade de produtos vendidos")
    produto=st.selectbox("Campo para escolher o produto vendido",["Zapflow com Gemini","Zapflow com ChatGpt","Zapflow com Llama"])
    
    if st.button("Salvar"):
        data_hora = datetime.combine(data,hora)
        st.write("**Dados da Venda:**")
        st.write(f"Email do Vendedor:{email}")
        st.write(f"Data e hora da Compra:{data_hora}")
        st.write(f"Valor da Venda: R${valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")
if __name__ == "__main__":
    main()
