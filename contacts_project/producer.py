import pika
import json
from faker import Faker
from models import Contact
import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_URI = os.getenv("RABBITMQ_URI")
fake = Faker()

def send_contacts_to_queue(queue_name, count=5):
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URI))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)

    for _ in range(count):
        contact = Contact(
            fullname=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            preferred_channel=fake.random_element(["email", "sms"])
        ).save()

        message = json.dumps({"contact_id": str(contact.id)})
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message)
        print(f"Додано контакт {contact.fullname} у чергу {queue_name}")

    connection.close()

if __name__ == "__main__":
    send_contacts_to_queue("email_queue", count=5)
    send_contacts_to_queue("sms_queue", count=5)
