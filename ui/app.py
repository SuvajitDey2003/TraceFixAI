import streamlit as st
import requests

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(
    page_title="TraceFix AI",
    page_icon="🛠️",
    layout="centered"
)

import os

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/analyze"
)


# ----------------------------
# UI
# ----------------------------
st.title("🛠️ TraceFix AI")
st.caption("GenAI + RAG powered Debugging Assistant")

st.markdown(
    """
Paste an error message or stack trace below.
TraceFix AI will analyze the **root cause**, suggest a **fix**,  
and explain **how to prevent it** using real-world knowledge.
"""
)

error_log = st.text_area(
    "Error / Stack Trace",
    height=180,
    placeholder="Example: IndexError: list index out of range"
)

analyze = st.button("Analyze Error", type="primary")

# ----------------------------
# ACTION
# ----------------------------
if analyze:
    if not error_log.strip():
        st.warning("Please paste an error message.")
    else:
        with st.spinner("Analyzing error..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"error_log": error_log},
                    timeout=30
                )

                if response.status_code == 200:
                    result = response.json()
                    st.success("Analysis Complete")
                    st.markdown(result["analysis"])
                else:
                    st.error("Backend error occurred.")
                    st.code(response.text)

            except requests.exceptions.RequestException as e:
                st.error("Unable to connect to backend API.")
                st.code(str(e))

# ----------------------------
# FOOTER
# ----------------------------
st.divider()
st.caption("Built with FastAPI, FAISS, Groq & Streamlit")
