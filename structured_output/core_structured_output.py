from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from typing import List , Optional

load_dotenv()


model = ChatGroq(
    model = "openai/gpt-oss-120b"
)

class Movie(BaseModel):
    title : str
    release_year : int
    genre : List[str]
    cast : List[str]
    Rating : Optional[float]
    summary : str


parser = PydanticOutputParser(pydantic_object=Movie)


prompt = ChatPromptTemplate.from_messages([
    ('system',
    """
Extract movie information from the movie name
    {formate_instruction}
"""),
('human', 
"{movie_name}"),
])

name = input("Enter your movie Name:")

final_prompt = prompt.invoke(
    {'movie_name' : name,
    'formate_instruction' : parser.get_format_instructions()
    }
)

response = model.invoke(final_prompt)
final_response = parser.parse(response.content)

print(final_response)