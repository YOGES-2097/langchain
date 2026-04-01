from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

os.environ["GOOGLE_API_KEY"] = api_key

def init_gemini_model(max_tokens=300):
    """Initializes the Gemini model with the specified maximum tokens."""
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", max_tokens=max_tokens)
    return llm