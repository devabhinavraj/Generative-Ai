import streamlit as st

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel
from typing import List, Optional

# -------------------- Load -------------------- #

load_dotenv()

# -------------------- Model -------------------- #

model = ChatGroq(
    model="openai/gpt-oss-120b"
)

# -------------------- Schema -------------------- #

class Movie(BaseModel):
    title: str
    release_year: int
    genre: List[str]
    cast: List[str]
    Rating: Optional[float]
    summary: str

parser = PydanticOutputParser(
    pydantic_object=Movie
)

# -------------------- Prompt -------------------- #

prompt = ChatPromptTemplate.from_messages(
[
(
"system",
"""
Extract movie information from the movie title.

{format_instruction}
"""
),
(
"human",
"{movie_name}"
)
]
)

# -------------------- UI -------------------- #

st.set_page_config(
    page_title="Structured Output Demo",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Structured Output")

movie_name = st.text_input(
    "Movie Name",
    placeholder="Interstellar"
)

if st.button("Generate"):

    with st.spinner("Generating..."):

        final_prompt = prompt.invoke(
            {
                "movie_name": movie_name,
                "format_instruction": parser.get_format_instructions()
            }
        )

        response = model.invoke(final_prompt)

        movie = parser.parse(response.content)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📦 Structured Output")

        st.write(movie)

    with col2:

        st.subheader("📄 JSON Output")

        st.json(movie.model_dump())