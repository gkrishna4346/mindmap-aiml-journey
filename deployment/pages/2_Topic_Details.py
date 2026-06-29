import streamlit as st
import pandas as pd
from pathlib import Path


# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Topic Details",
    layout="wide"
)


# ---------------------------------
# LOAD CSV
# ---------------------------------

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


df = df.fillna(
    "nan"
)


# ---------------------------------
# CSS
# ---------------------------------

st.markdown(
"""
<style>

/* =========================
PAGE
========================= */

.block-container{

overflow:visible !important;

padding-top:2rem;

padding-left:2rem;

padding-right:2rem;

max-width:100%;

}


/* =========================
HERO
========================= */

/* STICKY HERO WRAPPER */

div:has(> .hero){

position:sticky !important;

top:12px !important;

z-index:9999 !important;

align-self:flex-start;

}


.hero{

background:
linear-gradient(
90deg,
#071426,
#09192d
);

padding:18px;

border-radius:18px;

border:1px solid #1f3b5a;

margin-bottom:18px;

color:white;

}



.hero h1{

font-size:30px;

font-weight:700;

margin-bottom:12px;

color:white;

}


.hero-body{

font-size:20px;

font-weight:600;

color:white;

}


/* =========================
CARDS
========================= */

.topic-card{

background:#071426;

border:1px solid #1e3550;

border-radius:16px;

padding:12px 16px;

margin-bottom:14px;

}


.card-title{

font-size:30px;

font-weight:800;

margin-bottom:8px;

line-height:1.1;

color:inherit;

}


.card-content{

color:white;

font-size:20px;

line-height:1.5;

padding-top:0px;

}


/* =========================
BADGES
========================= */

.badge{

display:inline-block;

padding:8px 16px;

border-radius:12px;

margin-right:14px;

font-size:16px;

font-weight:700;

color:white;

}


.badge-blue{

background:#0d6efd;

}


.badge-purple{

background:#6f42c1;

}


/* =========================
SEARCH
========================= */

div[data-testid="stTextInput"]{

margin-bottom:10px !important;

}


div[data-testid="stTextInput"] > div{

height:70px !important;

}


div[data-testid="stTextInput"] input{

height:70px !important;

font-size:20px !important;

font-weight:500 !important;

color:#5f6368 !important;

-webkit-text-fill-color:#5f6368 !important;

opacity:0.80 !important;

padding-left:18px !important;

padding-right:18px !important;

padding-top:0px !important;

padding-bottom:0px !important;

line-height:50px !important;

}


/* Placeholder */

div[data-testid="stTextInput"] input::placeholder{

font-size:20px !important;

font-weight:500 !important;

opacity:0.8 !important;

line-height:50px !important;

}


/* Press Enter */

div[data-testid="InputInstructions"]{

display:flex !important;

align-items:center !important;

height:50px !important;

font-size:14px !important;

color:#808080 !important;

}


/* =========================
SIDEBAR
========================= */

section[data-testid="stSidebar"] *{

font-size:15px !important;

}


section[data-testid="stSidebar"] button{

font-size:15px !important;

font-weight:500 !important;

}


/* =========================
HEADERS
========================= */

.topic-card h3{

font-size:30px !important;

font-weight:800 !important;

line-height:1.1 !important;

margin-bottom:10px !important;

}


.topic-card h4{

font-size:28px !important;

font-weight:800 !important;

line-height:1.1 !important;

margin-bottom:10px !important;

}

/* NAV CAPSULE */

[data-testid="column"]:last-child{

padding-top:10px;

}

.stButton button{

height:40px !important;

border-radius:30px !important;

border:1px solid #2d415c !important;

background:white !important;

font-size:34px !important;

box-shadow:none !important;

}


.stButton button:hover{

border-color:#4e7dff !important;

transform:scale(1.02);

}

</style>
""",
unsafe_allow_html=True
)


# ---------------------------------
# SEARCH & NAVIGATION
# ---------------------------------
st.markdown(
"""
<div style='height:18px;'></div>
""",
unsafe_allow_html=True
)



search_col, nav_col = st.columns(
    [5, 2]
)

with search_col:

    search = st.text_input(
        "",
        placeholder="🔍 Search another topic",
        label_visibility="collapsed"
    )


with nav_col:

    c1, c2, c3 = st.columns([1,1,1])

    with c1:

        if st.button(
                "◀︎",
                key="prev_top",
                use_container_width=True
        ):
            st.session_state[
                "nav_action"
            ] = "prev"

    with c2:

        if st.button(
                "🏠",
                key="home_top",
                use_container_width=True
        ):
            st.switch_page(
                "app.py"
            )

    with c3:

        if st.button(
                "▶︎",
                key="next_top",
                use_container_width=True
        ):
            st.session_state[
                "nav_action"
            ] = "next"

if search:

    matches = df[

        df["topic"]

        .astype(str)

        .str.lower()

        .str.contains(

            search.lower(),

            na=False

        )

        |

        df["search_keywords"]

        .astype(str)

        .str.lower()

        .str.contains(

            search.lower(),

            na=False

        )

    ]


    if not matches.empty:

        st.session_state[
            "selected_topic"
        ] = matches.iloc[0][
            "topic"
        ]


# ---------------------------------
# VALIDATION
# ---------------------------------

if (
    "selected_topic"
    not in st.session_state
):

    st.info(
        "Select topic from Home Page"
    )

    st.stop()


topic = st.session_state[
    "selected_topic"
]


row = df[

    df[
        "topic"
    ] == topic

]

st.markdown(
"""
</div>
""",
unsafe_allow_html=True
)

if row.empty:

    st.warning(
        "Topic not found"
    )

    st.stop()


row = row.iloc[0]

# -------------------------
# NAVIGATION EXECUTION
# -------------------------

if "nav_action" in st.session_state:

    action = st.session_state[
        "nav_action"
    ]

    del st.session_state[
        "nav_action"
    ]

    if action == "prev":

        prev_topic = str(
            row[
                "previous_topic"
            ]
        ).strip()

        if prev_topic != "-":

            st.session_state[
                "selected_topic"
            ] = prev_topic

            st.rerun()


    if action == "next":

        next_topic = str(
            row[
                "next_topic"
            ]
        ).strip()

        if next_topic != "-":

            st.session_state[
                "selected_topic"
            ] = next_topic

            st.rerun()

# -----------------------
# CATEGORY & LEVEL
# -----------------------

category = str(
    row[
        "category"
    ]
)

level = str(
    row[
        "level"
    ]
)

# Hero

st.markdown(
f"""
<div class="hero">

<h1>
🌲 Topic: {row["topic"]}
</h1>

<div style="margin-top:18px;">

<span class="badge badge-blue">
{category}
</span>

<span class="badge badge-purple">
{level}
</span>

</div>

</div>
""",
unsafe_allow_html=True
)


# ---------------------------------
# MAIN CONTENT
# ---------------------------------

left, right = st.columns(
    [2,1]
)


# =========================
# LEFT
# =========================

# =========================
# LEFT
# =========================

with left:

    sections = [

        (
            "📖 Intro",
            "intro",
            "#74c0fc"
        ),

        (
            "📘 Definition",
            "definition",
            "#7fffd4"
        ),

        (
            "💡 Simple Explanation",
            "simple_explanation",
            "#ffd166"
        ),

        (
            "🧪 Example",
            "example",
            "#90ee90"
        ),

        (
            "⚙️ How It Works",
            "how_it_works",
            "#87ceeb"
        ),

        (
            "⭐ Key Points",
            "key_points",
            "#ffb347"
        )

    ]


    for title, col, color in sections:

        st.markdown(
f"""
<div class='topic-card'>

<h3
class="card-title"
style="color:{color};"
>

{title}

</h3>

<div class='card-content'>

{row[col]}

</div>

</div>
""",
unsafe_allow_html=True
        )


    # =========================
    # PROS & CONS
    # =========================

    st.markdown(
    """
    <div style='height:10px;'></div>
    """,
    unsafe_allow_html=True
    )


    pros_col, cons_col = st.columns(
        [1,1]
    )


    with pros_col:

        st.markdown(
f"""
<div class='topic-card'>

<h3 style='color:#90ee90;'>

✅ Pros

</h3>

<div class='card-content'>

{row["pros"]}

</div>

</div>
""",
unsafe_allow_html=True
        )


    with cons_col:

        st.markdown(
f"""
<div class='topic-card'>

<h3 style='color:#ff9e80;'>

❌ Cons

</h3>

<div class='card-content'>

{row["cons"]}

</div>

</div>
""",
unsafe_allow_html=True
        )

# =========================
# RIGHT
# =========================

with right:


    cards = [

        (
            "📌 Prerequisite",
            "prerequisite",
            "#ffa94d"
        ),

        (
            "🔗 Related Topics",
            "related_topics",
            "#ff6b6b"
        ),

        (
            "🎯 Use Cases",
            "use_cases",
            "#87ceeb"
        ),


        (
            "📦 Libraries",
            "libraries",
            "#d8b4fe"
        ),

        (
            "🧠 Remember This",
            "remember_this",
            "#7fffd4"
        ),

        (
            "💻 Code",
            "code",
            "#4dabf7"
        ),

        (
            "⚡ Quick Facts",
            "quick_facts",
            "#ffd166"
        ),
        (
            "🔎 Search Keywords",
            "search_keywords",
            "#74c0fc"
        )

    ]


    for title, col, color in cards:


        st.markdown(
f"""
<div
class='topic-card'
>

<h4
style='
color:{color};
margin-bottom:16px;
'>

{title}

</h4>

<div
class='card-content'
>

{row[col]}

</div>

</div>
""",
unsafe_allow_html=True
        )


# ---------------------------------
# FOOTER
# ---------------------------------

st.caption(
"""
MindMap: AIML Journey • Built by Gopikrishna 
"""
)
