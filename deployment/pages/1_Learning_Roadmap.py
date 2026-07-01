# ============================================
# MindMap: AIML Journey
# Index Page - Version 2 Development
# ============================================


import streamlit as st
import pandas as pd
from pathlib import Path


# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="Learning Roadmap",
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
# LEARNING MODULES
# -------------------------

modules = [

    {
        "icon": "📘",
        "title": "AI Foundations",
        "start": 1,
        "end": 18
    },

    {
        "icon": "📗",
        "title": "Machine Learning",
        "start": 19,
        "end": 66
    },

    {
        "icon": "📙",
        "title": "Deep Learning",
        "start": 67,
        "end": 99
    },

    {
        "icon": "📕",
        "title": "Natural Language Processing",
        "start": 100,
        "end": 111
    },

    {
        "icon": "📒",
        "title": "Generative AI & LLM",
        "start": 112,
        "end": 132
    },

    {
        "icon": "📓",
        "title": "Responsible AI",
        "start": 133,
        "end": 136
    },

    {
        "icon": "📔",
        "title": "Advanced Machine Learning",
        "start": 137,
        "end": 180
    }

]

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

<h1>📚 Learning Roadmap</h1>

<p>
Structured learning path from AI Foundations to Advanced Deep Learning.
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
# LEARNING ROADMAP
# -------------------------

st.subheader("📚 Learning Roadmap")

# -------------------------
# TOTAL TOPICS
# -------------------------

total_topics = len(df)

st.caption(

f"{total_topics} Topics • {len(modules)} Learning Modules"

)

st.write("")

for module_no, module in enumerate(modules, start=1):

    module_df = df[
        (df["display_order"] >= module["start"]) &
        (df["display_order"] <= module["end"])
    ]

    with st.expander(

        f'{module["icon"]} Module {module_no} — {module["title"]} • {len(module_df)} Topics',

        expanded=False

    ):

        for _, row in module_df.iterrows():

            if st.button(

                f'{int(row["display_order"]):02d} │ {row["topic"]}',

                key=row["topic"],

                use_container_width=True

            ):

                st.session_state["selected_topic"] = row["topic"]

                st.switch_page(
                    "pages/2_Topic_Details.py"
                )


st.caption(
"""
MindMap: AIML Journey • Built by Gopikrishna 
"""
)