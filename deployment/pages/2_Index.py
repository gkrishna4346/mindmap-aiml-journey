import streamlit as st
import pandas as pd
from pathlib import Path


# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="Topic Index",
    layout="wide"
)


# -------------------------
# LOAD CSV
# -------------------------

ROOT = (
    Path(__file__)
    .resolve()
    .parents[2]
)

CSV_PATH = (
    ROOT
    / "data"
    / "topics.csv"
)


try:

    df = pd.read_csv(
        CSV_PATH,
        encoding="utf-8"
    )

except:

    df = pd.read_csv(
        CSV_PATH,
        encoding="latin1"
    )


df = df.fillna("-")


# -------------------------
# CSS
# -------------------------

st.markdown(
"""
<style>

.topic-btn{

padding:16px;

background:#071426;

border:1px solid #1f3b5a;

border-radius:14px;

margin-bottom:14px;

font-size:24px;

font-weight:600;

color:white;

}

.topic-btn:hover{

border:1px solid #5d88ff;

}

.hero-index{

background:linear-gradient(
90deg,
#071426,
#09192d
);

padding:28px;

border-radius:18px;

margin-bottom:24px;

}

.hero-index h1{

font-size:42px;

font-weight:800;

margin-bottom:10px;

color:#ffffff !important;

}

.hero-index p{

font-size:20px;

font-weight:500;

color:#d6e4ff !important;

margin-bottom:20px;

opacity:1;

}

.topic-count{

display:inline-block;

background:#0d6efd;

padding:10px 18px;

border-radius:12px;

font-size:18px;

font-weight:700;

color:white !important;

}

div.stButton > button{

text-align:left !important;

padding-left:25px !important;

height:58px !important;

font-size:40px !important;

border-radius:14px !important;

transition:0.2s;

}

div.stButton > button:hover{

transform:translateX(10px);

border:1px solid #4f8cff;

}
</style>
""",
unsafe_allow_html=True
)

# -------------------------
# HOME BUTTON
# -------------------------

left, center, right = st.columns(
    [0.5,1,1]
)

with left:

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):

        st.switch_page(
            "app.py"
        )


st.write("")

# -------------------------
# TITLE
# -------------------------

st.markdown(
"""
<div class='hero-index'>

<h1>📚 Topic Index</h1>

<p>
Explore all available AIML topics
</p>

</div>
""",
unsafe_allow_html=True
)



# -------------------------
# SEARCH
# -------------------------

search = st.text_input(
    "",
    placeholder="🔍 Search Topic",
    label_visibility="collapsed"
)


if search:

    df = df[

        df["topic"]

        .astype(str)

        .str.lower()

        .str.contains(
            search.lower(),
            na=False
        )

    ]


# -------------------------
# TOPICS
# -------------------------

for idx, row in df.iterrows():

    button_style = f"""
    <style>

    div.stButton > button{{
    text-align:left !important;

    justify-content:flex-start !important;

    padding-left:25px !important;

    font-size:22px !important;

    height:60px !important;

    border-radius:14px !important;

    }}

    </style>
    """

    st.markdown(
        button_style,
        unsafe_allow_html=True
    )

    if st.button(

            f"{idx + 1:02d} • {row['topic']}",

            use_container_width=True,

            key=row["topic"]

    ):

        st.session_state[
            "selected_topic"
        ] = row[
            "topic"
        ]

        st.switch_page(
            "pages/1_Topic_Details.py"
        )

st.caption(
"""
MindMap: AIML Journey • Built by Gopikrishna 
"""
)