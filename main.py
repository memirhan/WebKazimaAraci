import requests
from bs4 import BeautifulSoup as bs

url = "https://stackoverflow.com/questions/tagged/python-requests?tab=newest&page=1&pagesize=50"

response = requests.get(url)
parser = bs(response.text, "html.parser")

articles = parser.find_all("div", {"class": "s-post-summary"})  # Classı s-post-summary olan tüm içerikleri aldık

for article in articles:
    baslik = article.find("h3", {"class": "s-post-summary--content-title"})
    aciklama = article.find("div", {"class": "s-post-summary--content-excerpt"})
    goruntulenme = article.find("div", {"class": "s-post-summary--stats-item "})
    tagsContainer = article.find("div", {"class": "tags"}) 

    tags = []
    if tagsContainer:
        tagElements = tagsContainer.find_all("a", {"class": "post-tag"})
        for tag in tagElements:  # tagElement listesindeki her bir a elementi için çalışır.
            tags.append(tag.text)

    if baslik and aciklama:
        print("--------------------------------------")
        print(baslik.text)
        print(aciklama.text.strip())
        print("\n")
        print(" ".join(tags) if tags else "Etiket bulunamadı")