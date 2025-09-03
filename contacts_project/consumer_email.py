import pika
import json
from models import Contact
import os
from dotenv import load_dotenv

load_dotenv()
RABBITMQ_URI = os.getenv("RABBITMQ_URI")

def send_email_stub(contact):
    print(f"Надсилаємо email {contact.fullname} ({contact.email})")
    contact.sent = True
    contact.save()

def callback(ch, method, properties, body):
    data = json.loads(body)
    contact_id = data["contact_id"]
    contact = Contact.objects(id=contact_id).first()
    if contact:
        send_email_stub(contact)
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URI))
channel = connection.channel()
channel.queue_declare(queue="email_queue", durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="email_queue", on_message_callback=callback)

print("Чекаємо повідомлень")
channel.start_consuming()

