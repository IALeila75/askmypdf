import os
from dotenv import load_dotenv
import streamlit as st
import requests

# ─── Config ─────────────────────────────────────────────────────────────────
load_dotenv(dotenv_path="../.env")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("🗂️ Chat PDF (Front-end)")

# 1) Upload
pdf = st.file_uploader("Téléversez votre PDF", type="pdf")
if pdf:
    with st.spinner("Traitement en cours…"):
        res = requests.post(
            f"{BACKEND_URL}/upload",
            files={"file": (pdf.name, pdf.getvalue(), "application/pdf")}
        )
    if res.status_code != 200:
        st.error(f"Upload échoué : {res.text}")
        st.stop()

    doc_id = res.json()["doc_id"]
    st.success(f"Document traité ! ID : `{doc_id}`")

    # 2) Chat
    question = st.text_input("Posez votre question")
    if question:
        with st.spinner("Recherche de réponse…"):
            qres = requests.get(
                f"{BACKEND_URL}/query",
                params={"doc_id": doc_id, "q": question}
            )
        if qres.status_code == 200:
            st.markdown(f"**Réponse :** {qres.json()['answer']}")
        elif qres.status_code == 429:
            st.error("Quota OpenAI dépassé : réessayez plus tard.")
        else:
            st.error(f"Erreur {qres.status_code} : {qres.text}")
