from utils.langchain_utils import init_gemini_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

llm = init_gemini_model()

def translate_text(text, target_language):
    prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a professional translator. Translate the following text into {language}. Only return the translated text."),
    ("user", "{text}")
    ])

    chain = prompt_template | llm
    response = chain.invoke({"language": target_language, "text": text})
    return response.content

if __name__ == "__main__":
    
    original_text = "Hello, how are you today? I hope you are having a productive day of coding."
    target = "japanese" 
    
    print(f"Original: {original_text}")
    print(f"Translating to {target}...")
    
    translated = translate_text(original_text, target)
    
    print("-" * 30)
    print(f"Result: {translated}")