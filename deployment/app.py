import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path


# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="MindMap: AIML Journey",
    layout="wide"
)


# ---------------------------------
# PATHS
# ---------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

LOGO_PATH = (
    BASE_DIR
    / "images"
    / "logo_mindmap3.jpg"
)

CSV_PATH = (
    BASE_DIR
    / "data"
    / "topics.csv"
)


# ---------------------------------
# LOAD DATA
# ---------------------------------

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


df = df.fillna("nan")


# ---------------------------------
# CUSTOM CSS
# ---------------------------------

st.markdown(
"""
<style>

.block-container{

padding-top:2rem;
padding-left:3rem;
padding-right:3rem;

}

.title{

font-family:
"Bernard MT Condensed",
Georgia,
serif;

font-size:58px;

font-weight:400;

color:#071426;

}

.subtitle{

font-size:22px;
color:#808080;

}

.topic-card{

padding:14px;
text-align:center;

}

.topic-title{

font-size:18px;
font-weight:600;
height:60px;

}

div.stButton > button{

width:100%;
height:44px;

border-radius:12px;

}

footer{

visibility:hidden;

}

</style>
""",
unsafe_allow_html=True
)


# ---------------------------------
# HEADER
# ---------------------------------

logo_col, text_col = st.columns([1,6])

with logo_col:

    if LOGO_PATH.exists():

        logo = Image.open(
            LOGO_PATH
        )

        st.image(
            logo,
            width=120
        )


with text_col:

    st.markdown(
        """
        <div class='title'>
        MindMap: AIML Journey
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='subtitle'>
        Search • Learn • Revise • Continue Journey
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")

index_left, index_center, index_right = st.columns(
    [2,2,2]
)

with index_center:

    if st.button(
        "📚 Index / Contents",
        use_container_width=True
    ):

        st.switch_page(
            "pages/2_Index.py"
        )


st.write("")
# ---------------------------------
# SEARCH
# ---------------------------------

left, center, right = st.columns([1,4,1])

with center:

    search = st.text_input(
        "",
        placeholder="🔍 Try: AI | Machine Learning | NLP",
        label_visibility="collapsed"
    )


if search:

    search = search.lower()

    matches = df[

        df["topic"]

        .astype(str)

        .str.lower()

        .str.contains(
            search,
            na=False
        )

        |

        df["search_keywords"]

        .astype(str)

        .str.lower()

        .str.contains(
            search,
            na=False
        )

    ]


    if not matches.empty:

        st.session_state[
            "selected_topic"
        ] = matches.iloc[0]["topic"]


        st.switch_page(
            "pages/1_Topic_Details.py"
        )


st.write("")
st.write("")


# ---------------------------------
# QUICK TOPICS
# ---------------------------------

st.subheader(
    "Quick Topics"
)


topics = [

("🧠","Artificial Intelligence"),

("📊","Data Science"),

("🔎","Exploratory Data Analysis"),

("🧩","Machine Learning"),

("🧬","Deep Learning")

]


st.markdown(
"""
<style>

.topic-icon{

font-size:40px;

margin-bottom:10px;

}

.topic-title{

display:flex;

align-items:center;

justify-content:center;

}

</style>
""",
unsafe_allow_html=True
)


left, center, right = st.columns(
    [1,6,1]
)


with center:

    cols = st.columns(5)


    for i, (
        icon,
        title
    ) in enumerate(
        topics
    ):


        with cols[i]:

            st.markdown(
f"""
<div class='topic-card'>

<div class='topic-icon'>
{icon}
</div>

<div class='topic-title'>
{title}
</div>

</div>
""",
unsafe_allow_html=True
            )


            if st.button(
                "Open Topic",
                key=f"topic_{i}",
                use_container_width=True
            ):


                st.session_state[
                    "selected_topic"
                ] = title


                st.switch_page(
                    "pages/1_Topic_Details.py"
                )


st.divider()

# ---------------------------------
# EXPLORE LEARNING PATH
# ---------------------------------

st.subheader(
    "Explore Learning Path"
)


path = [

"Artificial Intelligence",

"Data Science",

"Exploratory Data Analysis",

"Machine Learning",

"Deep Learning"

]


st.markdown(
"""
<style>

.path-box{

height:70px;

display:flex;

align-items:center;

justify-content:center;

text-align:center;

border:1px solid #E8E8E8;

border-radius:14px;

background:#F8F8FC;

font-size:18px;

font-weight:600;

padding:10px;

}


.arrow{

text-align:center;

font-size:34px;

padding-top:14px;

color:#888;

}

</style>
""",
unsafe_allow_html=True
)


cols = st.columns(
[
3,
0.6,
3,
0.6,
3,
0.6,
3,
0.6,
3
]
)


for i in range(
    len(path)
):


    with cols[
        i*2
    ]:


        st.markdown(
f"""
<div class='path-box'>

{path[i]}

</div>
""",
unsafe_allow_html=True
        )


    if i < len(path)-1:


        with cols[
            (i*2)+1
        ]:


            st.markdown(
"""
<div class='arrow'>

→

</div>
""",
unsafe_allow_html=True
            )


st.write("")


st.info(
"""
Future enhancement: More topics will be added.
Refer Index page for the currently updated topics.
"""
)


st.divider()


# ---------------------------------
# FOOTER
# ---------------------------------

st.caption(
"""
MindMap: AIML Journey • Built by Gopikrishna 
"""
)