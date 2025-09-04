import json
from parse_quotes import scrape_quotes
from parse_authors import scrape_authors


if __name__ == "__main__":
    print("Парсинг цитат")
    quotes, authors_links = scrape_quotes()

    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)

    print(f"Збережно {len(quotes)} цитати в quotes.json")

    print("Парсинг авторів")
    authors = scrape_authors(authors_links)

    with open("authors.json", "w", encoding="utf-8") as f:
        json.dump(authors, f, ensure_ascii=False, indent=4)

    print(f"Збережено {len(authors)} авторів в authors.json")
    print("Завершено")

