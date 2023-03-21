from tortoise import Model
from tortoise.fields import IntField, CharField


class User(Model):
    id: IntField = IntField(pk=True)  # Primary key (Autoincrement)
    uid: IntField = IntField(null=True)  # Telegram User ID
    nickname: CharField = CharField(max_length=128, null=True)  # User name

