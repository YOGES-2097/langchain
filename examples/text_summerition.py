from utils.langchain_utils import init_gemini_model
from langchain_core.messages import HumanMessage
from langchain_core.summarize import load_summarize_chain
from langchain_core.documents import Document

llm = init_gemini_model()
text = """
The Naruto series follows the life of a young ninja who is ostracized by his village 
because he contains the spirit of a Nine-Tailed Fox. Despite the prejudice, Naruto 
dreams of becoming the Hokage, the village leader. Along the way, he forms deep 
bonds with his teammates, especially Sasuke Uchiha and Sakura Haruno. The story 
evolves into an epic conflict involving the Akatsuki and the legendary Uchiha 
ancestors, eventually leading to the Fourth Shinobi World War where Naruto 
must reconcile with the past to save the future.
"""

docs = [Document(page_content=text)]

def run_summarization():
    print("--- Starting Summarization ---")
    chain = load_summarize_chain(llm, chain_type="stuff")
    result = chain.invoke(docs)
    
    print("\nSummary:")
    print(result["output_text"])

if __name__ == "__main__":
    run_summarization()