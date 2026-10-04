import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####

st.title("Galvão Bueno CEP")

##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]



##### BARRA LATERAL #####

st.sidebar.title("Qual é o CEP Arnaldo ?")
st.sidebar.image("logo.png", width=400)
st.sidebar.write("Aplicação para buscar endereço a partir do CEP e entrar localização no mapa.")
escolha = st.sidebar.selectbox("Escolha uma opção", opcoes)

##### BOTÃO BUSCAR CEP #####

if escolha == "Buscar CEP":
    st.header("Buscar Endereço pelo CEP")
    cep = st.text_input("Digite o CEP (somente números):")

    if st.button("Buscar"):
            if len(cep) !=8 or not cep.isdigit():
                  st.error("Por favor, insira um CEP válido com 8 dígitos numéricos.")
            else:
                try:
                    endereco = BuscarCep.buscar_cep(cep)
                    if endereco:
                         st.success("Endereço encontrado:")
                         st.write(f"CEP: {endereco[0]}")
                         st.write(f"Endereço: {endereco[1]}")
                         st.write(f"Bairro: {endereco[2]}")
                         st.write(f"Cidade: {endereco[3]}")
                         st.write(f"Estado: {endereco[4]}")

                         ## Mapas
                         st.title("Localização no mapa")
                         df = pd.DataFrame({"latitude": [endereco[5]], "longitude": [endereco[6]]})
                         st.map(df, zoom=15)
                    else:
                        st.error("CEP não encontrado.")
                except Exception as e:
                    st.error(f"Ocorreu um erro ao buscar o CEP: {e}")

##### BOTÃO DESCOBRIR CEP #####

elif escolha == "Descobrir CEP":
    st.header("Descobrir CEP pelo Endereço")
    endereco_usuario = st.text_input("Digite o endereço (ex: Rua Olga, Barueri, SP):")

    if st.button("Descobrir"):
        if not endereco_usuario.strip():
             st.error("Por favor, digite um Endereço válido.")

        else:
            try:
                resultado = BuscarCep.descobrir_cep(endereco_usuario)
                st.success("Link de busca no Google:")
                st.write(resultado)
            except Exception as e:
                st.error(f"Ocorreu um erro aon descobrir o CEP: {e}")
