from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="moonshot-v1-8k",
                  openai_api_key=api_key,
                  openai_api_base="https://api.moonshot.cn/v1")
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
            ("system", system_template_text),
            ("human", human_template_text)
            ])
from langchain.output_parsers import PydanticOutputParser

output_parser = PydanticOutputParser()
parser_instructions = output_parser.get_format_instructions()

result = (prompt | model | output_parser).invoke(
                   {"input_language": input_language,
                    "parser_instructions": parser_instructions})
