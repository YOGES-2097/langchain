from utils.langchain_utils import init_gemini_model
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage

llm = init_gemini_model()
template = "Rephrase this sentence in a more professional and polite tone: {sentence}"
prompt_template = PromptTemplate.from_template(template)
user_sentence = "i need a project immediately"
formatted_prompt = prompt_template.format(sentence=user_sentence)
response = llm.invoke([HumanMessage(content=formatted_prompt)])
print("-" * 30)
print(f"Original User Message:\n{user_sentence}")
print("-" * 30)
print(f"Professional Rephrasing:\n{response.content}")
print("-" * 30)