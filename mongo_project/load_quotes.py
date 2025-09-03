import json
import os
from models import Author, Quote

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
quotes_file = os.path.join(BASE_DIR, 'quotes.json')

with open(quotes_file, 'r', encoding='utf-8') as f:
    quotes = json.load(f)

for item in quotes:
    author = Author.objects(fullname=item['author']).first()
    if not author:
        print(f'Автор {item["author"]} не знайден у базі, додайте автора.')
        continue

    if not Quote.objects(quote=item['quote'], author=author):
        quote = Quote(
            quote=item['quote'],
            author=author,
            tags=item.get('tags', []),
        )
        quote.save()
        print(f'Додано цитату автора: {author.fullname}: "{quote.quote}"')
    else:
        print(f'Цитата від {author.fullname} вже існує')
