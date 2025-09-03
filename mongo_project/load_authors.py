import json
import os
from models import Author

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
authors_file = os.path.join(BASE_DIR, 'authors.json')

with open(authors_file, 'r', encoding='utf-8') as f:
    authors = json.load(f)

for item in authors:
    if not Author.objects(fullname=item['fullname']):
        author = Author(
            fullname=item['fullname'],
            born_date=item.get('born_date', ''),
            born_location=item.get('born_location', ''),
            description=item.get('description', '')
        )
        author.save()
        print(f'Додано автора: {author.fullname}')
    else:
        print(f'Автор {item["fullname"]} вже існує')
