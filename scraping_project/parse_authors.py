import requests
from bs4 import BeautifulSoup


def scrape_authors(authors_links):
    authors_data = []

    for link in authors_links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")

        fullname = soup.find("h3", class_="author-title").get_text(strip=True)
        born_date = soup.find("span", class_="author-born-date").get_text(strip=True)
        born_location = soup.find("span", class_="author-born-location").get_text(strip=True)
        description = soup.find("div", class_="author-description").get_text(strip=True)

        authors_data.append({
            "fullname": fullname,
            "born_date": born_date,
            "born_location": born_location,
            "description": description
        })

    return authors_data
