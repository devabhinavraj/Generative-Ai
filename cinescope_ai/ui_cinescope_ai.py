import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# -------------------- Page Config -------------------- #
st.set_page_config(
    page_title="CineScope AI",
    page_icon="🎬",
    layout="centered",
)

# -------------------- Custom CSS -------------------- #
st.markdown(
    """
    <style>

    .main{
        padding-top:2rem;
    }

    h1{
        text-align:center;
        font-weight:800;
        font-size:3rem;
    }

    .sub{
        text-align:center;
        color:#9ca3af;
        margin-bottom:2rem;
    }

    .stButton>button{
        width:100%;
        height:52px;
        border-radius:14px;
        font-size:17px;
        font-weight:600;
        transition:0.25s;
    }

    .stButton>button:hover{
        transform:translateY(-2px);
    }

    div[data-testid="stTextInput"] input{
        height:52px;
        border-radius:14px;
        font-size:17px;
    }

    .block-container{
        max-width:850px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- LLM -------------------- #

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)

prompt = ChatPromptTemplate.from_messages(
[
(
"system",
"""
You are CineScope AI, a professional movie information assistant.

The user will provide a movie title.

Movie Title: {movie_name}

Return accurate movie information.
"""
),
("human","Movie Title: {movie_name}")
]
)

# -------------------- Header -------------------- #

st.title("🎬 CineScope AI")

st.markdown(
"<p class='sub'>Search any movie and get complete information in seconds.</p>",
unsafe_allow_html=True
)

movie_name = st.text_input(
    "",
    placeholder="🍿 Search a movie... (e.g. Interstellar, 3 Idiots, Inception)"
)

search = st.button("✨ Search Movie")

# -------------------- Result -------------------- #

if search:

    if movie_name.strip() == "":
        st.warning("Enter a movie title.")
        st.stop()

    with st.spinner("Finding movie details... 🍿"):

        final_prompt = prompt.invoke(
            {
                "movie_name": movie_name
            }
        )

        response = llm.invoke(final_prompt)

    st.markdown("---")

    st.markdown(response.content)