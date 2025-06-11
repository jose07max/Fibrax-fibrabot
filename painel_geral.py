import streamlit as st

st.set_page_config(page_title="FibraBot Painel", layout="centered")

st.title("🤖 Painel de Controle – FibraBot")
st.write("Automação inteligente para Fibrax Telecom")

# Importa os módulos
import agendador_de_postagens as agendador
import respostas_automaticas as respostas
import sugestoes_virais as sugestoes
import fibrax_whatsapp_bot as whatsapp

# Layout de botões
col1, col2 = st.columns(2)

with col1:
    if st.button("📅 Agendador de Postagens"):
        agendador.run()

    if st.button("🔥 Sugestões de Conteúdos Virais"):
        sugestoes.run()

with col2:
    if st.button("💬 Respostas Automáticas"):
        respostas.run()

    if st.button("🤖 Bot WhatsApp (360dialog)"):
        whatsapp.run()

st.caption("FibraBot desenvolvido para Fibrax Telecom – Todos os direitos reservados ©")