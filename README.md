# chatbot_permis
Objectifs
Un projet d'entraînement pour créer un chatbot intelligent permettant de s'exercer au code de la route.

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

git clone https://github.com/Fatalmoudou/chatbot_permis
cd chatbot-permis
2. Créer un environnement virtuel

python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows
3. Installer les dépendances

pip install -r requirements.txt

4. Répartition des tâches

->Futur Software Engineer
 Backend (FastAPI)
Créer l’API pour exposer les endpoints /quiz et /answer.
Gérer les routes utilisateurs et l’authentification basique (optionnel).
Intégrer le LLM (LangChain ou API OpenAI).
Développer les services métiers (vérification des réponses, logique de quiz).
Intégration MongoDB
Connecter le backend à MongoDB.

Gérer les opérations CRUD sur les questions et utilisateurs.
Créer un schéma propre pour les collections (questions, users, logs).
LLM
Mettre en place l’intégration avec LangChain ou Hugging Face.
 Développer la logique de RAG si nécessaire (connexion avec MongoDB/FAISS).
Tests & Documentation
Écrire des tests unitaires pour l’API.
Documenter les endpoints avec Swagger (inclus dans FastAPI).

👩‍💻 Futur Data Engineer
Scraping des données
Identifier les sources légales de questions de code.
 Écrire un script BeautifulSoup pour récupérer les questions et réponses.
Nettoyer et transformer les données avec Pandas.
Pipeline Data
Automatiser l’insertion des données nettoyées dans MongoDB.
Gérer les mises à jour et les doublons.
Structurer les scripts d’ETL pour qu’ils soient réutilisables.
Indexation et recherche
Mettre en place un moteur de recherche (MongoDB Atlas Search ou FAISS).
Générer les embeddings (si RAG implémenté).
Analyse des données
Créer des notebooks pour analyser la qualité des données.
Suivre les statistiques d’utilisation du chatbot.
