import pandas as pd
import json
import requests
import streamlit as st

# Configuração
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# Carregar Dados
perfil = json.load(open("data/perfil_investidor.json"))
historico = pd.read_csv("data/historico_atendimento.csv")
transacoes = pd.read_csv("data/transacoes.csv")
produtos = json.load(open("data/produtos_financeiros.json"))

# Montando Contexto
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# System Prompt
SYSTEM_PROMPT = """Você é o DIN-DIN, um modelo de IA com foco em cálculos e estratégias financeiras.

Objetivo:
O principal objetivo é manter o cliente positivo, se ele estiver negativado então o desafio se torna positivar as finanças do usuário.

Regras:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras nem de qualquer outra finalidade
3. Se não souber algo, admita e recalcule
4. Você deve ser direto sempre e mostrar que de pouco em pouco se constrói muito
5. sempre garante que o usuário entendeu os cálculos e as possibilidades..."""

# Chamar Ollama
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# Interface
st.title("DIN-DIN, seu Assistente Financeiro")

if pergunta := st.chat_input("Calculando as finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
