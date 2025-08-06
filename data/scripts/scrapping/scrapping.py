import requests
from bs4 import BeautifulSoup
import json
import re

#url du site du scrapping
URL = "https://codedelaroute.io/blog/question-theorique-examen-permis-de-conduire/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

data = []
#quand on fait une inspection du site on remarque que les questions sont sous forme de listes à puce
uls = soup.find_all("ul")

for ul in uls:
    # pour chaque ul on recupère li 
    question_li = ul.find("li")
    #si le li est en "strong c'est que normalement c'est une question"
    if question_li and question_li.strong:
        #donc on recupère cette question pour trouver le id 
        question_title = question_li.strong.get_text(strip=True)
        # la on fait le regex explication : Exemple on a un truc du genre : Question 03 (VI)
        # \s : pour l'espace
        # (\d) representre un nombre avec la parenthèse c'est un groupe de nombre 
        # \s pour un autre espace 
        #\( pour la parenthèse 
        #(.*?) pour le groupe de n'importe quoi 
        match = re.match(r"Question\s+(\d+)\s*\((.*?)\)", question_title)
        if match:
            question_id = match.group(1)# le groupe de nombre
            question_type = match.group(2)# le groupe de n'importe quoi

            # Récupérer le paragraphe suivant c'est là où les questions se trouvent 
            next_p = ul.find_next_sibling("p")
            if next_p:
                elements = next_p.find_all(["strong"])
                current_question = None
                current_category = None

                for el in elements:
                    text = el.get_text(strip=True)

                    if text.startswith("Question"):
                        current_category = text.replace("Question", "").strip()
                        # extraire la question qui suit immédiatement ce <strong>
                        question_text = el.next_sibling.strip(" :«»") if el.next_sibling else ""
                        current_question = {
                            "id": f"{question_id}-{len(data)+1}",
                            "type": question_type,
                            "category": current_category,
                            "question": question_text,
                            "answer": ""
                        }
                        data.append(current_question)

                    elif text.startswith("Réponse") and current_question:
                        answer_text = el.next_sibling.strip(" :«»") if el.next_sibling else ""
                        current_question["answer"] = answer_text

print(f"{len(data)} questions trouvées")

with open("data/raw/questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
