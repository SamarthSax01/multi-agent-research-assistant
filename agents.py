from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tool import web_search,read_webpage
from dotenv import load_dotenv
load_dotenv()
llm=ChatMistralAI(model="mistral-small-2506")

def build_search_agent():
    return create_agent(model=llm,tools=[web_search])
def build_read_agent() :
    return create_agent(model=llm,tools=[read_webpage])

writer_prompt=ChatPromptTemplate.from_messages(
    [
        ("system",""" you are an expert research writer write clear
         ,structured and insightful points"""),("human",""" write 
                                                a detailed research report
                                                on the topic below
                                                Topics:{topic}
                                                Reseach:{research}
                                                structure the report as :
                                                INTRODUCTION
                                                KEY FINDINGS
                                                CONCLUSION 
                                                SOURCES
                                                BE PROFESSIONAL """)
    ]
)
writer_chain=writer_prompt|llm|StrOutputParser()

critic_prompt=ChatPromptTemplate.from_messages(
    [
        ("system","""You are a sharp and constructive research critic. Be honest and specific."""),
        ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
...""")
    ]
)
critic_chain=critic_prompt|llm|StrOutputParser()
 