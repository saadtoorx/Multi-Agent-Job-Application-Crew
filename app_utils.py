import os
import pprint

def enter_and_set_api_keys(streamlit_mode=True):
    """
    Prompts the user to enter OpenAI and Serper API keys and sets them as environment variables.
    Works for both Streamlit and CLI modes.
    Returns the entered keys as a tuple: (openai_api_key, serper_api_key)
    """
    if streamlit_mode:
        import streamlit as st
        openai_api_key = st.text_input("OpenAI API Key", type="password")
        serper_api_key = st.text_input("Serper API Key", type="password")
        if not openai_api_key or not serper_api_key:
            st.warning("Please enter both OpenAI and Serper API keys to continue.")
            # Don't use st.stop() here - let the main app handle the conditional display
            return "", ""  # Return empty strings instead of stopping
    else:
        openai_api_key = input("OpenAI API Key: ")
        serper_api_key = input("Serper API Key: ")
        if not openai_api_key or not serper_api_key:
            print("Both OpenAI and Serper API keys are required.")
            exit(1)
    
    # Only set environment variables if both keys are provided
    if openai_api_key and serper_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key
        os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"
        os.environ["SERPER_API_KEY"] = serper_api_key
    
    return openai_api_key, serper_api_key

def pretty_print_result(result):
    """
    Pretty print the result dictionary in a readable format.
    """
    pprint.pprint(result)