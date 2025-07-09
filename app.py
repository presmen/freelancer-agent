# app.py

import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Freelancer Financial Guidance Agent", layout="centered")
st.title("💼 Freelancer Financial Guidance Agent")
st.subheader("Get tailored financial advice for your freelance journey")

user_input = st.text_area("🧠 Tell me about your freelance work, income, and financial goals:")

if st.button("Get Financial Guidance"):
    if user_input.strip() != "":
        response = run_agent(user_input)
        st.markdown("### 🤖 Agent Insight")
        st.write(response)
    else:
        st.warning("Please describe your financial situation so I can help!")

st.markdown("---")
st.markdown("💡 _Built by Preshit Mendhekar · Strategic intelligence for independent professionals._")
