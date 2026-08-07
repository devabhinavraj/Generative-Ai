import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.6,
    max_tokens=1000
)

# Personality selection
choice = st.radio(
    "Choose your AI's personality:",
    ["Funny", "Professional", "Friendly", "Sarcastic"],
    horizontal=True
)

# Initialize chat history in session state
if "chat_history" not in st.session_state or st.session_state.get("current_choice") != choice:
    st.session_state.chat_history = [
        SystemMessage(content=f"You are a {choice} assistant.")
    ]
    st.session_state.current_choice = choice

# Display past messages (skip the SystemMessage)
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# Chat input
query = st.chat_input("Type your message...")

if query:
    st.session_state.chat_history.append(HumanMessage(content=query))
    with st.chat_message("user"):
        st.write(query)

    response = model.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)