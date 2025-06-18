
#  Chat avec PDF (RAG + LLM en Français)

Ce projet vous permet de discuter avec n'importe quel document PDF en utilisant :
-  RAG (Retrieval Augmented Generation)
-  Embeddings locaux (`sentence-transformers`)
-  Modèle instruct français (`plguillou/t5-base-fr-sum-cnndm`)
-  Interface utilisateur avec Streamlit

---

##  Structure du projet

```
askmypdf/
├── backend/        # API FastAPI (RAG, FAISS, QA)
│   └── main.py
├── frontend/       # App Streamlit
│   └── app.py
├── .env            # Variables d’environnement (API key, etc.)
├── requirements.txt
└── README.md
```

---

##  Lancer l’application en local

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/askmypdf.git
cd askmypdf
```

### 2. Créer l’environnement

```bash
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Ajouter le fichier `.env`

Créez un fichier `.env` à la racine avec :

```ini
OPENAI_API_KEY=sk-xxxxx (optionnel)
HF_TOKEN=hf_xxxxx (optionnel)
```

### 4. Lancer le back-end (API FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

### 5. Lancer le front-end (Streamlit)

Dans un **deuxième terminal** :

```bash
cd frontend
streamlit run app.py
```

---

##  Déploiement Cloud

###  Option 1 : Hugging Face Spaces (Streamlit)

1. Aller sur https://huggingface.co/spaces
2. Créer un nouveau Space : `SDK = Streamlit`
3. Uploader le dossier `frontend/` (et `.env si besoin`)
4. Ajouter vos secrets via l’onglet `Settings > Secrets`

###  Option 2 : Render.com ou Railway (API FastAPI)

- Créez un nouveau projet Python
- Déployez uniquement le dossier `backend/`
- Ajoutez un fichier `render.yaml` ou `Procfile` si nécessaire
- Ajoutez vos variables dans les Settings

---

##  Exemple de modèle utilisé

Le modèle T5 français utilisé :

```python
from transformers import pipeline
pipe = pipeline("summarization", model="plguillou/t5-base-fr-sum-cnndm")
```

---

## 📎 Ressources utiles

-  [Dataset PDF à tester](https://huggingface.co/datasets?)
-  [plguillou/t5-base-fr-sum-cnndm](https://huggingface.co/plguillou/t5-base-fr-sum-cnndm)
-  [Notebook local](./chat_pdf_local_test_fr.ipynb)

---

##  À venir

- Ajout d’un résumé automatique dès upload
- Détection de la langue du PDF
- Support pour plusieurs modèles LLM locaux

---
