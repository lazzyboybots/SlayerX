import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("8726992"))
API_HASH = getenv("fbf4bc635f74937b9669af1d715171c9")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7845383477:AAHYzyEga5ppCJwFKRYogCWlBzMP3VmKYs4")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002490973872"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("7743411008"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/lazzyboybots/SlayerX",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    ""
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Lazzy_Bots_Official")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Lazzy_Bots_Support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("")
SPOTIFY_CLIENT_SECRET = getenv("")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQCFKdAAUeGC7Mo8Jw7FcSYanIY92UyPl7fjS6yFCz-KEohqt5AjP-AQWkBbTNwOaCYeudgWTKwe1l8tJTiYhEaWF_krFZBCoCeC-dYpyhJBpfWwc7pBSoZfY9Lp1tpUFxCZEs0oJG2DD4HCKyr2cVjixG3tfD80DgpDj2KgrL5yGxk0-FwOSfi3sBVOa2y7QgkYhSlakVwmf64rLO8HwJkCc3rrAVcDYRIiGCqctcmVUAkJqsOCgzMVNihu7v1RJfHuYOyybdzP1627iRTTfVhf7zzRDFC08cVNgfn1S4YKLXEe_hv2o2CY1AAVst3XrMZ9xXUFvxVK-JsTHU4cIwWqz8Tn6wAAAAHNixNAAA")
STRING2 = getenv("BQCFKdAAUeGC7Mo8Jw7FcSYanIY92UyPl7fjS6yFCz-KEohqt5AjP-AQWkBbTNwOaCYeudgWTKwe1l8tJTiYhEaWF_krFZBCoCeC-dYpyhJBpfWwc7pBSoZfY9Lp1tpUFxCZEs0oJG2DD4HCKyr2cVjixG3tfD80DgpDj2KgrL5yGxk0-FwOSfi3sBVOa2y7QgkYhSlakVwmf64rLO8HwJkCc3rrAVcDYRIiGCqctcmVUAkJqsOCgzMVNihu7v1RJfHuYOyybdzP1627iRTTfVhf7zzRDFC08cVNgfn1S4YKLXEe_hv2o2CY1AAVst3XrMZ9xXUFvxVK-JsTHU4cIwWqz8Tn6wAAAAHNixNAAA")
STRING3 = getenv("BQCFKdAAUeGC7Mo8Jw7FcSYanIY92UyPl7fjS6yFCz-KEohqt5AjP-AQWkBbTNwOaCYeudgWTKwe1l8tJTiYhEaWF_krFZBCoCeC-dYpyhJBpfWwc7pBSoZfY9Lp1tpUFxCZEs0oJG2DD4HCKyr2cVjixG3tfD80DgpDj2KgrL5yGxk0-FwOSfi3sBVOa2y7QgkYhSlakVwmf64rLO8HwJkCc3rrAVcDYRIiGCqctcmVUAkJqsOCgzMVNihu7v1RJfHuYOyybdzP1627iRTTfVhf7zzRDFC08cVNgfn1S4YKLXEe_hv2o2CY1AAVst3XrMZ9xXUFvxVK-JsTHU4cIwWqz8Tn6wAAAAHNixNAAA")
STRING4 = getenv("BQCFKdAAUeGC7Mo8Jw7FcSYanIY92UyPl7fjS6yFCz-KEohqt5AjP-AQWkBbTNwOaCYeudgWTKwe1l8tJTiYhEaWF_krFZBCoCeC-dYpyhJBpfWwc7pBSoZfY9Lp1tpUFxCZEs0oJG2DD4HCKyr2cVjixG3tfD80DgpDj2KgrL5yGxk0-FwOSfi3sBVOa2y7QgkYhSlakVwmf64rLO8HwJkCc3rrAVcDYRIiGCqctcmVUAkJqsOCgzMVNihu7v1RJfHuYOyybdzP1627iRTTfVhf7zzRDFC08cVNgfn1S4YKLXEe_hv2o2CY1AAVst3XrMZ9xXUFvxVK-JsTHU4cIwWqz8Tn6wAAAAHNixNAAA")
STRING5 = getenv("BQCFKdAAUeGC7Mo8Jw7FcSYanIY92UyPl7fjS6yFCz-KEohqt5AjP-AQWkBbTNwOaCYeudgWTKwe1l8tJTiYhEaWF_krFZBCoCeC-dYpyhJBpfWwc7pBSoZfY9Lp1tpUFxCZEs0oJG2DD4HCKyr2cVjixG3tfD80DgpDj2KgrL5yGxk0-FwOSfi3sBVOa2y7QgkYhSlakVwmf64rLO8HwJkCc3rrAVcDYRIiGCqctcmVUAkJqsOCgzMVNihu7v1RJfHuYOyybdzP1627iRTTfVhf7zzRDFC08cVNgfn1S4YKLXEe_hv2o2CY1AAVst3XrMZ9xXUFvxVK-JsTHU4cIwWqz8Tn6wAAAAHNixNAAA")


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/db7653b29f9b702cb12f8.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/bc7f8903e60fbfafa2eb4.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://graph.org/file/2fd73ef39c62047594009.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
