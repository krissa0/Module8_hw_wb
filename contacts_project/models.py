from mongoengine import Document, StringField, EmailField, BooleanField, connect
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
connect(host=MONGO_URI)

class Contact(Document):
    fullname = StringField(required=True)
    email = EmailField(required=True)
    phone = StringField()
    sent = BooleanField(default=False)
    preferred_channel = StringField(choices=["email", "sms"], default="email")

    def __str__(self):
        return f"{self.fullname} ({self.email}) - Sent: {self.sent}"
