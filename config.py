from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BAGo3K8AW5vG-uV9LNNiA2b4QnDas4Cf73yjEFCNOUbLfJ6gNit7h6YwyaEzZf39OLhd-lBWCEr0fwWjIz8IL8ip5jvcmBucL2HjBIUy1upZ7qDhorT3a-1x4mwehxsNaORgIJtumbQDD_Nvnma3lBs14gpedRMSUGTtzHSMndHRzSmaKno4pzh5S5lYRMS09INKzIu5axiVlOn5Sa_0J4Z6ou38h2IhXdnsIY1o5Rz05hz7M-n1cM0Tr_A4VG_djAocmx2CZXURG2zNgjWjL1sTY1EMsY6OpLiuu7rcdHUwU2RpkEaEUXfFEZ1P2qZxq5YvsIOAoOAv7Uc_3m42z2muzl8gAAAAF43cWXAA")
BOT_TOKEN = getenv("BOT_TOKEN", "6581228589:AAEiEFwA8qpTSy1CQAtI8iFkZDGSh-O6YYs")
BOT_NAME = getenv("BOT_NAME", "Epik Test") 
API_ID = int(getenv("API_ID", "27843759"))
API_HASH = getenv("API_HASH", "3d221e95ddabbc281a0347698584e0aa")
BOT_USERNAME = getenv("BOT_USERNAME", "EpikTestBot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 500))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6181368568").split()))
