import os
from mongoengine import connect, Q
from dotenv import load_dotenv
from models import Author, Quote

load_dotenv()
MONGO_URI = os.getenv("MONGODB_URI")

connect(host=MONGO_URI)

print("Пошук цитат. Використовуй команди: name:ім'я, tag:тег, tags:тег1,тег2, exit для виходу.")

while True:
    command = input(">>> ").strip()

    if command.lower() == "exit":
        print("Вихід")
        break

    if command.startswith("name:"):
        name_query = command[len("name:"):].strip()
        authors = Author.objects(fullname__icontains=name_query)
        quotes_list = []
        for author in authors:
            quotes_list.extend(Quote.objects(author=author))
        if quotes_list:
            for q in quotes_list:
                print(f"{q.author.fullname}: {q.quote}")
        else:
            print("Цитат не знайдено.")

    elif command.startswith("tag:"):
        tag_query = command[len("tag:"):].strip()
        quotes_list = Quote.objects(tags__icontains=tag_query)
        if quotes_list:
            for q in quotes_list:
                print(f"{q.author.fullname}: {q.quote}")
        else:
            print("Цитат не знайдено.")

    elif command.startswith("tags:"):
        tags_query = command[len("tags:"):].strip().split(",")
        query = Q()
        for t in tags_query:
            query |= Q(tags__icontains=t.strip())
        quotes_list = Quote.objects(query)
        if quotes_list:
            for q in quotes_list:
                print(f"{q.author.fullname}: {q.quote}")
        else:
            print("Цитат не знайдено.")

    else:
        print("Невірна команда. Використовуй name:, tag:, tags:, exit.")
