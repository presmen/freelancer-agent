import streamlit as st
from agent import run_agent

# Page settings
st.set_page_config(page_title="Freelancer Financial Guidance", page_icon="💼")

st.title("💼 Freelancer Financial Guidance Agent")
st.write("Describe your situation, and our intelligent agent will guide you toward the most relevant financial products.")

# Text input
user_input = st.text_area("🧠 Tell me about your freelance work and savings goals:", height=150)

# Button click
if st.button("Get Recommendations"):
    if user_input.strip():
        output = run_agent(user_input)

        st.subheader("🧠 Agent Insight")
        st.write(output["agent_response"])

        st.subheader("🔍 Recommended Products")
        for product in output["recommendations"]:
            st.markdown(f"**{product['name']}**")
            st.write(product["description"])
            st.divider()
    else:
        st.warning("Please enter something before clicking the button.")
