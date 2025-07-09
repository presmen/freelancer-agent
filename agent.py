import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from prompts import PROFILE_PROMPT
from matcher import find_best_match

import openai  # For usage tracking

# Initialize model with API key from .env
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.5,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

prompt = PromptTemplate(
    input_variables=["bio", "chat_history"],
    template="""
    You are a financial guidance agent.

    Chat History:
    {chat_history}

    New input:
    "{bio}"

    Based on this and prior context, summarize user needs, recommend product types, and ask a thoughtful follow-up question.
    """
)

agent_chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

def get_current_usage():
    try:
        usage = openai.BillingUsage.retrieve()
        total_spent = usage["total_usage"] / 100  # Convert cents to dollars
        return total_spent
    except Exception as e:
        return None  # Fails silently if API call fails

def run_agent(user_bio: str):
    # Set your soft budget here
    MAX_BUDGET = 8.0

    if get_current_usage() and get_current_usage() > MAX_BUDGET:
        agent_reply = "🛑 You’ve reached your usage budget. GPT responses are disabled for now."
    else:
        try:
            agent_reply = agent_chain.run(bio=user_bio)
        except Exception as e:
            agent_reply = "⚠️ GPT agent is unavailable. Here's a basic match using local logic."

    matches = find_best_match(user_bio)

    return {
        "agent_response": agent_reply,
        "recommendations": matches
    }
