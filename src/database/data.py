from tortoise import Model
from tortoise.fields import IntField, JSONField


class Data(Model):
    id: IntField = IntField(pk=True)  # Primary key (Autoincrement)
    days: JSONField = JSONField(
        default={
            "monday": {
                "10:00": None,
                "12:00": None,
                "14:00": None,
                "16:00": None,
                "18:00": None,
            },
            "tuesday": {
                "10:00": None,
                "12:00": None,
                "14:00": None,
                "16:00": None,
                "18:00": None,
            },
            "wednesday": {
                "10:00": None,
                "12:00": None,
                "14:00": None,
                "16:00": None,
                "18:00": None,
            },
            "thursday": {
                "10:00": None,
                "12:00": None,
                "14:00": None,
                "16:00": None,
                "18:00": None,
            },
            "friday": {
                "10:00": None,
                "12:00": None,
                "14:00": None,
                "16:00": None,
                "18:00": None,
            },
        }
    )
