import json
from pymongo import MongoClient

# Connexion à MongoDB (local ou cloud)
client = MongoClient('mongodb://localhost:27017/')  # modifie si cloud (Mongo Atlas)

# Choisir la base et la collection
db = client['permis_conduire']
collection = db['questions']

# Charger le fichier JSON (avec ta liste de QCM)
with open('data/processed/qcm.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Insertion dans la collection
# Si tu veux écraser les données avant, tu peux drop la collection
collection.drop()  

# Insert many documents
collection.insert_many(data)

print(f"{len(data)} questions insérées dans MongoDB.")
