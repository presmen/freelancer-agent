# 💼 Freelancer Financial Guidance Agent

An intelligent Streamlit-powered agent built with LangChain to help freelancers discover personalized financial products based on their savings goals, income style, and work profile.

## 🚀 Features
- GPT-powered agent with memory and reasoning
- Custom FAISS-based matcher for product recommendations
- Soft quota limiter to prevent OpenAI overuse
- Fallback mode to avoid crashes when API fails

## 🧠 How It Works
Users submit a short bio → the agent analyzes needs → recommends products from a curated catalog.

## 🛠 Tech Stack
- LangChain
- OpenAI GPT-3.5
- Streamlit
- FAISS
- dotenv

## ⚙️ Setup
```bash
pip install -r requirements.txt
streamlit run app.py

## 📚 Author

Built by [Preshit Mendhekar](https://www.linkedin.com/in/preshitmendhekar), a seasoned Product Owner and Business Process Architect actively transitioning into Product Management.  
Specialized in fintech, innovation strategy, and intelligent product ecosystems.
