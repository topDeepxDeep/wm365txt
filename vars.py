#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "3498045"))
API_HASH = environ.get("API_HASH", "229441a8b355de58ba025be657c82ea3")
BOT_TOKEN = environ.get("BOT_TOKEN", "8373086447:AAEmSLV-Q85ZtvrX2VCeiTHuYWDCmTOeP7E")

OWNER = int(environ.get("OWNER", "6478217960"))
CREDIT = environ.get("CREDIT", "ᴹᴿ🌿⃝🅺ιʟͥʟͣᴇᷟʀ✍࿐ཽ༵")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6478217960').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6478217960').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

