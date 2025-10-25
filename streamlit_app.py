import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to OpenAI using your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Streamlit Page Setup ---
st.set_page_config(page_title="CultureBot GPT", page_icon="🦜", layout="centered")
st.title("🦜 CultureBot GPT – Philippine Culture Assistant")
st.write("Ask me about Philippine heroes, myths, or literature! 🇵🇭")

# --- Chat Section ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are CultureBot GPT, a friendly Filipino storyteller."}
    ]

# Input box
user_input = st.chat_input("Ask CultureBot something...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state["messages"],
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = "⚠️ Sorry, I couldn’t connect to OpenAI right now."

    st.chat_message("assistant").write(answer)
    st.session_state["messages"].append({"role": "assistant", "content": answer})
