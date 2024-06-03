from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class llm():
  
  def llm_responce(text):    
    prompt = ChatPromptTemplate.from_messages(
        [
          ("system" , "You need to provide me relevant answer based on the question I ask you. Make sure to keep the answer consise and precise"),
          ("user" , "Question:{question}")     
        ]  
    )

    llm = Ollama(model = "llama2")

    output_parser = StrOutputParser()

    chain = prompt|llm|output_parser


    answer = chain.invoke({"question" :  text})
    
    return answer
  

