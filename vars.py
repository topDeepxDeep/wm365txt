#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27473563"))
API_HASH = environ.get("API_HASH", "bc2ea0765ac96bb474891b0243f44390")
BOT_TOKEN = environ.get("BOT_TOKEN", "7086145092:AAELtQW8GMdkA5UOHknyrY89zOXDv8TjZTU")

OWNER = int(environ.get("OWNER", "6363345131"))
CREDIT = environ.get("CREDIT", "ᴹᴿ🌿⃝🅺ιʟͥʟͣᴇᷟʀ✍࿐ཽ༵")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6363345131,6478217960').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6478217960').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


