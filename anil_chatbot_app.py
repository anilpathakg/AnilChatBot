import streamlit as st
from openai import OpenAI
import os

# API Key (will be set in Streamlit Cloud later, not here)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

st.title("💬 My AI Chatbot")

if "conversation" not in st.session_state:
    st.session_state.conversation = [
        {"role": "system", "content": "You are a helpful chatbot."}
    ]

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    st.session_state.conversation.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.conversation
    )
    reply = response.choices[0].message.content
    st.session_state.conversation.append({"role": "assistant", "content": reply})

for msg in st.session_state.conversation[1:]:  # skip system message
    role = "👤 You" if msg["role"] == "user" else "🤖 Bot"
    st.write(f"**{role}:** {msg['content']}")
