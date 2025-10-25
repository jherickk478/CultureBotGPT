# streamlit_app.py
import streamlit as st
from culturebot_gpt import ask_culturebot
import time

# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="CultureBot GPT 🇵🇭",
    page_icon="🦜",
    layout="centered"
)

# --- Custom Filipino Theme & Style ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to bottom right, #0038A8, #CE1126);
        background-attachment: fixed;
        color: #1a1a1a;
        font-family: 'Segoe UI', sans-serif;
    }
    .chat-container {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        margin-top: 20px;
        max-height: 70vh;
        overflow-y: auto;
    }
    .chat-message {
        padding: 10px 15px;
        border-radius: 15px;
        margin: 10px 0;
        line-height: 1.5;
        animation: fadeIn 0.4s ease-in;
    }
    .user {
        background-color: #ffde59;
        text-align: right;
        font-weight: 500;
    }
    .assistant {
        background-color: #f1f1f1;
        border-left: 5px solid #0038A8;
        font-weight: 500;
    }
    .title {
        text-align: center;
        font-size: 2.5rem;
        color: white;
        font-weight: 900;
        margin-top: 10px;
        text-shadow: 1px 1px 2px #00000066;
    }
    .subtitle {
        text-align: center;
        color: #FFD700;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .stButton>button {
        background-color: #FFD700;
        color: #0038A8;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.2rem;
        font-weight: bold;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #0038A8;
        color: white;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="title">🦜 CultureBot GPT</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your friendly Filipino culture assistant 🇵🇭</div>', unsafe_allow_html=True)
st.write("---")

# --- Chat State ---
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# --- Clear Chat Button ---
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# --- Chat Container ---
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            st.markdown(f'<div class="chat-message user">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message assistant">{msg["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- User Input ---
user_input = st.chat_input("Ask CultureBot something...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.markdown(f'<div class="chat-message user">{user_input}</div>', unsafe_allow_html=True)

    # Generate response
    with st.spinner("CultureBot is thinking... 🤔"):
        answer = ask_culturebot(user_input)
        time.sleep(0.5)

    # --- Typing animation ---
    typing_placeholder = st.empty()
    typed_text = ""
    for char in answer:
        typed_text += char
        typing_placeholder.markdown(f'<div class="chat-message assistant">{typed_text}</div>', unsafe_allow_html=True)
        time.sleep(0.01)

    st.session_state["messages"].append({"role": "assistant", "content": answer})
