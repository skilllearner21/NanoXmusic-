from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/625926bd0a3af4167942e.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/518f95567d95f9e7ddcf6.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/learningbots79")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/official_learning_bots_Support")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5016109398").split()))


FAILED = "https://graph.org/file/625926bd0a3af4167942e.jpg"
