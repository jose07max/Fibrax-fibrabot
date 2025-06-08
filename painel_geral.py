import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="FibraBot - Painel Geral", layout="wide")

# Autenticação simples
usuarios = {
    "admin@fibrax.com.br": "fibrax123",
    "suporte@fibrax.com.br": "suporte2024"
}

st.title("🔒 Login - Painel FibraBot")

login_usuario = st.text_input("Usuário (e-mail)")
login_senha = st.text_input("Senha", type="password")
autenticado = False

if st.button("Entrar"):
    if login_usuario in usuarios and usuarios[login_usuario] == login_senha:
        st.success("Login realizado com sucesso!")
        autenticado = True
    else:
        st.error("Usuário ou senha incorretos.")

if autenticado:
    st.title("📊 Painel Geral - FibraBot (Fibrax Telecom)")

    # Carregar métricas simuladas
    try:
        df = pd.read_csv("metricas.csv")
    except:
        st.error("Erro ao carregar 'metricas.csv'. Certifique-se que ele está na mesma pasta do painel.")

    # Seção 1: Métricas gerais
    st.header("📈 Métricas da Semana")
    col1, col2, col3 = st.columns(3)
    col1.metric("Seguidores", df['seguidores'].iloc[-1])
    col2.metric("Curtidas", df['curtidas'].sum())
    col3.metric("Comentários", df['comentarios'].sum())

    # Seção 2: Gráficos
    st.subheader("📉 Evolução Diária")
    tab1, tab2 = st.tabs(["Curtidas e Comentários", "Seguidores"])

    with tab1:
        fig, ax = plt.subplots()
        ax.plot(df['data'], df['curtidas'], label="Curtidas", marker='o')
        ax.plot(df['data'], df['comentarios'], label="Comentários", marker='s')
        ax.set_ylabel("Qtd")
        ax.set_title("Engajamento")
        ax.legend()
        st.pyplot(fig)

    with tab2:
        fig2, ax2 = plt.subplots()
        ax2.plot(df['data'], df['seguidores'], color='green', marker='x')
        ax2.set_ylabel("Seguidores")
        ax2.set_title("Crescimento")
        st.pyplot(fig2)

    # Seção 3: Links para outras funções (instruções)
    st.header("🛠️ Funcionalidades Disponíveis")
    st.markdown("""
    - Agendador de Postagens → `agendador_de_postagens.py`
    - Respostas Automáticas → `respostas_automaticas.py`
    - Sugestões de Conteúdos Virais → `sugestoes_virais.py`
    - Bot WhatsApp (360dialog) → `fibrax_whatsapp_bot.py`
    """)

    st.caption("FibraBot desenvolvido para Fibrax Telecom - Todos os direitos reservados ©")