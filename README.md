# chatbot_permis
Objectifs
Créer un chatbot capable de poser des questions de type QCM et de donner des corrections.

Stocker les données dans MongoDB.

Intégrer un LLM (LangChain, OpenAI ou modèle open source) pour répondre à des questions en langage naturel.

Automatiser la collecte de données grâce au scraping.

Construire un pipeline simple de suivi des utilisateurs et de leurs scores.

🛠️ Technologies utilisées
Backend : FastAPI

Base de données : MongoDB

Data Processing : Python (Pandas)

LLM / IA : LangChain, Hugging Face

Scraping : BeautifulSoup

Dashboard (optionnel) : Streamlit

Vector Search (optionnel) : FAISS ou MongoDB Atlas Search

📂 Structure du projet
bash
Copier
Modifier
chatbot-permis/
│
├── backend/
│   ├── main.py              # Point d'entrée FastAPI
│   ├── routes/              # Endpoints API
│   ├── models/              # Modèles Pydantic
│   └── services/            # Logique métier (quiz, LLM, etc.)
│
├── data/
│   ├── questions.json       # Questions QCM initiales
│   └── scripts/             # Scripts scraping / pipeline
│
├── notebooks/               # Exploration des données
│
├── requirements.txt         # Dépendances Python
└── README.md
🚀 Installation
1. Cloner le projet
bash
Copier
Modifier
git clone https://github.com/votre-utilisateur/chatbot-permis.git
cd chatbot-permis
2. Créer un environnement virtuel
bash
Copier
Modifier
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
3. Installer les dépendances
bash
Copier
Modifier
pip install -r requirements.txt
4. Configurer MongoDB
