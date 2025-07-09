# agent.py

import os
from langchain_community.chat_models import ChatOpenAI
from prompts import PROFILE_PROMPT

def run_agent(user_input):
    prompt = PROFILE_PROMPT.format(user_input=user_input)

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.5,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    response = llm.invoke(prompt)
    return response
