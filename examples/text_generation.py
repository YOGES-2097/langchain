from utils.langchain_utils import init_gemini_model 
from langchain.core.messages import HumanMessage

def generate_text():
    llm = init_gemini_model()
    prompt = "explain about naruto and obito"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

if __name__ == "__main__":
    print(generate_text())