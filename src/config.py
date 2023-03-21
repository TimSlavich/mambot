from envparse import env

env.read_envfile(".env")

BOT_TOKEN = env.str("BOT_TOKEN")
ADMIN_IDS = [1734816882, 430864002]
