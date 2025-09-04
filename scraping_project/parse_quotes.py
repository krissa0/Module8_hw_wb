import requests
from bs4 import BeautifulSoup


BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    quotes_data = []
    authors_links = set()
    url = BASE_URL

    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")
        for q in quotes:
            text = q.find("span", class_="text").get_text()
            author = q.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]

            # сохраняем цитату
            quotes_data.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

            link = q.find("a")["href"]
            authors_links.add(BASE_URL + link)

        next_btn = soup.find("li", class_="next")
        if next_btn:
            url = BASE_URL + next_btn.find("a")["href"]
        else:
            url = None

    return quotes_data, authors_links

