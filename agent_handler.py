import os
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_pandas_dataframe_agent

def create_agent(df: pd.DataFrame):
    """
    Creates a Pandas DataFrame agent powered by Google's Gemini Pro model.

    Args:
        df: The Pandas DataFrame to be analyzed.

    Returns:
        A LangChain agent.
    """
    # Instantiate the Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite-preview-06-17",
        temperature=0,
        convert_system_message_to_human=True  # Important for agent compatibility
    )

    # Create and return the Pandas DataFrame agent
    return create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        handle_parsing_errors=True,
        allow_dangerous_code=True
    )
