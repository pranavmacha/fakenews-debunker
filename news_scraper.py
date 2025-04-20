import requests
from bs4 import BeautifulSoup
from googlesearch import search

def get_related_articles(query, num=3):
    urls = list(search(query, num_results=num))
    articles = []

    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = ' '.join(p.get_text() for p in soup.find_all('p'))
            articles.append({'title': url, 'text': text, 'url': url})
        except Exception as e:
            print(f"Error with {url}: {e}")
            continue

    return articles

