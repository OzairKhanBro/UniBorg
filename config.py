# PLEASE STOP!
# DO NOT EDIT THIS FILE
# Create a new config.py file in same dir and import, then extend this class.
import os
from telethon.tl.types import ChatBannedRights

class Config(object):
    LOGGER = True
    # Get this value from my.telegram.org! Please do not steal
    APP_ID = int(os.environ.get("APP_ID", 628904))
    API_HASH = os.environ.get("API_HASH", "3cb5be81d643f4731817a838ade1a26e")
    # string session for running on Heroku
    # some people upload their session files on GitHub or other third party hosting
    # websites, this might prevent the un-authorized use of the
    # confidential session files
    HU_STRING_SESSION = os.environ.get("HU_STRING_SESSION", "1BJWap1wBu4phWf43WSsiBR5cuW6yDXgkWIeSGZB95cje5sLQ6V0-p90JIhD7pjZDjIKixIF0aNX1-Nr_JdfoxJIwOIsm6fN0hwpKC6ODpXL6BYRhCpqO4lOCaVnZuD16FYHtaOoYllYvtqrn1tWO2Vi23raRJp07B_V0Q1la4byQbwe0x6LUO7E3jCtp_3qJ-UuXMRpE3uK1M1-OpOr49aE3pFygJPvnARoW3fqg1iR7-ANsoLfwY7hosJ0-g_0oHxZO27wpd6b3NnUry2vWN7HxSRDECaOCuGZ-v-ClxBc3385prI2rNtKLzsndoamWC_FDfX1JK5fExncdyiZaLlOqwT3G2bw=")
    # Get your own APPID from https://api.openweathermap.org/data/2.5/weather
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    # Get your own ACCESS_KEY from http://api.screenshotlayer.com/api/capture
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    # Send .get_id in any group to fill this value.
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID", -100123456789))
    # Send .get_id in any channel to fill this value. ReQuired for @Manuel15 inspiration to work!
    PRIVATE_CHANNEL_BOT_API_ID = int(os.environ.get("PRIVATE_CHANNEL_BOT_API_ID", -100123456789))
    # This is required for the plugins involving the file system.
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
    IBM_WATSON_CRED_USERNAME = os.environ.get("IBM_WATSON_CRED_USERNAME", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    # This is required for the hash to torrent file functionality to work.
    HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
    # This is required for the @telegraph functionality.
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "UniBorg")
    # Get a Free API Key from OCR.Space
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    # Send .get_id in any group with all your administration bots (added)
    G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -100123456789))
    # TG API limit. An album can have atmost 10 media!
    GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
    TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
    # Telegram BOT Token from @BotFather
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    #
    #
    # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
    # TG API limit. A message can have maximum 4096 characters!
    MAX_MESSAGE_SIZE_LIMIT = 4095
    # set blacklist_chats where you do not want userbot's features
    UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
    # maximum number of messages for antiflood
    MAX_ANTI_FLOOD_MESSAGES = 10
    # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None,
        view_messages=None,
        send_messages=True
    )
    # chat ids or usernames, it is recommended to use chat ids,
    # providing usernames means an additional overhead for the user
    CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
    # specify LOAD and NO_LOAD
    LOAD = []
    # foloowing plugins won't work on Heroku,
    # because of their ephemeral file system
    NO_LOAD = [
        "fwd",
        "telegraph",
        "afk",
        "gban"
    ]
    # Get your own API key from https://www.remove.bg/ or
    # feel free to use http://telegram.dog/Remove_BGBot
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    # Set to True if you want to block users that are spamming your PMs.
    NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", False))
    # define "spam" in PMs
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
    # send .get_id in any channel to forward all your NEW PMs to this group
    PM_LOGGR_BOT_API_ID = int(os.environ.get("PM_LOGGR_BOT_API_ID", "-100"))
    # For Databases
    # can be None in which case plugins requiring
    # DataBase would not work
    DB_URI = os.environ.get("DATABASE_URL", "postgres://hdemyjmysdymbk:015860c82d4b5096199f88c88fc4b905a5914126332564c9e67bc5c2ba535429@ec2-23-21-234-53.compute-1.amazonaws.com:5432/d2grph6g68ss9k")
    # number of rows of buttons to be displayed in .helpme command
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 5))
    # specify command handler that should be used for the plugins
    # this should be a valid "regex" pattern
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "\.")
    # specify list of users allowed to use bot
    # WARNING: be careful who you grant access to your bot.
    # malicious users could do ".exec rm -rf /*"
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    # VeryStream only supports video formats
    VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
    VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
