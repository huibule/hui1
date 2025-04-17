from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from 小红书2_template import xiaohongshu_template,user_template
from 小红书1_model import Xiaohongshu
def ok(subject,api_key):
    model = ChatOpenAI(model="moonshot-v1-8k",
                       openai_api_key=api_key,
                       openai_api_base="https://api.moonshot.cn/v1")
    prompt = ChatPromptTemplate.from_messages([
        ("system", xiaohongshu_template),
        ("human", user_template)
    ])
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    parser_instructions = output_parser.get_format_instructions()
    result = (prompt | model | output_parser).invoke(
        {"subject": subject,
         "parser_instructions": parser_instructions})
    return result

