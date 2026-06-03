import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# 1. Carrega a chave do arquivo .env
load_dotenv()

# Configura a Interface Visual
st.set_page_config(page_title="ChatBot Atendimento - Seguro Saúde S/A", page_icon="🛡️", layout="centered")
st.title("🛡️ ChatBot Atendimento - Seguro Saúde S/A")
st.subheader("Modelo B: Solução Contextual com Memória Avançada")
st.write("Protótipo de PLN integrado via LangChain para sustentação de conversas encadeadas.")
st.markdown("---")

# Inicializa a memória do chat no estado da sessão (Streamlit)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Inicializa o motor da IA (Llama 3.1 via Groq)
@st.cache_resource
def iniciar_ia():
    return ChatGroq(temperature=0.0, model="llama-3.1-8b-instant")

llm = iniciar_ia()

prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "Você é o assistente virtual da seguradora Seguro Saúde S/A. "
        "Seu objetivo é ajudar o usuário de forma prestativa sobre os planos de saúde disponíveis: Bronze, Prata e Ouro. "
        "ATENÇÃO EXTREMA: Você possui um módulo de memória ativado. Use o histórico de mensagens para contextualizar "
        "as respostas e identificar correferências. Se o usuário usar pronomes oblíquos como 'nele', 'disso', 'daquele' "
        "ou referências ocultas, busque no histórico qual plano (Bronze, Prata ou Ouro) ele está se referindo."
    )),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])
chain = prompt | llm

# Exibe o balão de boas-vindas padrão do experimento
if not st.session_state.chat_history:
    with st.chat_message("assistant"):
        st.write("Olá! Sou o assistente virtual da nossa seguradora. Como posso ajudar? Pergunte sobre nossos planos de saúde: Bronze, Prata ou Ouro.")

# Desenha na tela o histórico de mensagens acumuladas
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# Campo de Entrada de Texto do Usuário 
if user_input := st.chat_input("Digite sua mensagem para o teste..."):
    
    # Mostra o texto digitado pelo usuário
    with st.chat_message("user"):
        st.write(user_input)
    
    # Executa a chamada de API externa enviando a pergunta e a memória acumulada
    with st.chat_message("assistant"):
        with st.spinner("Processando resposta contextual..."):
            resposta = chain.invoke({
                "input": user_input,
                "chat_history": st.session_state.chat_history
            })
            texto_resposta = resposta.content
            st.write(texto_resposta)
            
            # Interface de Avaliação: Coleta a métrica de Acurácia
            st.write("")
            st.caption("Métrica Experimental (Acurácia das Respostas):")
            col1, col2 = st.columns([1, 5])
            with col1:
                st.button("👍 Sim", key=f"yes_{len(st.session_state.chat_history)}")
            with col2:
                st.button("👎 Não", key=f"no_{len(st.session_state.chat_history)}")
    
    # Salva os turnos na lista de memória para alimentar a próxima iteração
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.chat_history.append(AIMessage(content=texto_resposta))