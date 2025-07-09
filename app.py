# app.py

import streamlit as st
from agent import run_agent

# Set up the page configuration
st.set_page_config(page_title="Freelancer Financial Guidance Agent", layout="centered")

# Page header
st.title("💼 Freelancer Financial Guidance Agent")
st.subheader("Receive personalized financial advice tailored to freelance professionals")

# Text input for freelancer's query
user_input = st.text_area(
    label="🧠 Describe your freelance work, income pattern, and financial goals:",
    placeholder="e.g. I’m a freelance ESG consultant with project-based income. I want to improve savings, manage taxes, and scale into an advisory firm.",
    height=150
)

# Response trigger
if st.button("Get Financial Guidance"):
    if user_input.strip() != "":
        response = run_agent(user_input)
        st.markdown("### 🤖 Agent Insight")
        st.markdown(response)  # ✅ Bonus: enables bullet points and formatting
    else:
        st.warning("🚨 Please describe your financial situation so I can assist you meaningfully!")

# Optional footer for credibility
st.markdown("---")
st.markdown("💡 _Built by Preshit Mendhekar · Strategic intelligence for independent professionals._")
