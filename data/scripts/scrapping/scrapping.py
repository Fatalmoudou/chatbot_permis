from bs4 import BeautifulSoup
import json
import requests

url="https://codedelaroute.io/blog/question-theorique-examen-permis-de-conduire/"
headers={"User-agent": "Mozilla/5.0"}
response=requests.get(url,headers=headers)