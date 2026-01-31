import streamlit as st
import base64
from backend import get_rag_chain

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_icon="📄",
    page_title="Akbar RAG Assistant",
    layout="wide"
)

# ---------------- BASE64 UTILS ----------------
def get_img_as_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_img_as_base64("background.jpg")
logo_img = get_img_as_base64("logo2.png")

# ---------------- GLOBAL CSS (EXTENDED) ----------------
page_style = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpeg;base64,{bg_img}");
    background-size: 180%;
    background-position: top left;
    background-repeat: no-repeat;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stSidebar"] {{
    background: rgba(0,0,0,0.85);
}}

.rag-card {{
    border-radius: 12px;
    background: rgb(163 168 184 / 85%);
    box-shadow: 0 4px 8px rgb(18, 18, 18);
    padding: 50px;
    margin-bottom: 60px;
}}

.rag-title {{
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #ffc107;
}}

.rag-title span {{
    color: #04ECF0;
}}

.ask-btn {{
    background-color: #ffc107;
    color: black;
    border-radius: 6px;
    padding: 10px 24px;
    font-size: 16px;
    border: none;
    transition: 0.3s ease;
}}

.ask-btn:hover {{
    background-color: #000345;
    color: white;
}}

.footer {{
    text-align: center;
    font-size: 20px;
    color: #ffffff;
    margin-top: 40px;
}}
</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# ---------------- SIDEBAR (COPIED PATTERN) ----------------
with st.sidebar:
    st.image("logo2.png", use_container_width=True)

    st.markdown("""
    <style>
                
        .custom-text {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            color:#ffc107;
        }
        .custom-text span {
            color: #04ECF0;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<p class="custom-text"><span>Akbar</span> RAG <span>Assistant</span></p>',
        unsafe_allow_html=True
    )

    github_button_html = """
    <div style="text-align: center; margin-top: 50px;">
        <a class="ask-btn" href="https://github.com/Engr-Mujeeb-Rahman"
           target="_blank" rel="noopener noreferrer">
           Visit my GitHub
        </a>
    </div>
    """
    st.markdown(github_button_html, unsafe_allow_html=True)

    footer_html = """
    <div style="padding:10px; text-align:center;margin-top: 20px;">
        <p style="font-size:20px; color:#ffffff;">
            Made with ❤️ by Engr. Mujeeb Ur Rahman
        </p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

# ---------------- LOAD BACKEND ----------------
@st.cache_resource
def load_chain():
    return get_rag_chain()

chain = load_chain()

# ---------------- MAIN CONTENT ----------------
st.markdown("""
<div class="rag-card">
    <div class="rag-title">
        Document <span>Question Answering</span>
    </div>
</div>
""", unsafe_allow_html=True)

query = st.text_input("Ask a question from your document")

if st.button("Ask", key="ask_btn"):
    if not query.strip():
        st.warning("Ask a real question.")
    else:
        with st.spinner("Thinking..."):
            answer = chain.invoke(query)

        st.markdown("""
        <div class="rag-card">
            <h3>Answer</h3>
        """, unsafe_allow_html=True)

        st.write(answer)

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    © 2026 | Akbar RAG Assistant
</div>
""", unsafe_allow_html=True)
