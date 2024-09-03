import os
from dotenv import load_dotenv

load_dotenv()


class Links:

    HOST = "https://demo.opensource-socialnetwork.org"

    LOGIN_PAGE = f"{HOST}/login"
    NEWS_FEED_PAGE = f"{HOST}/home"
    FRIENDS_PAGE = f"{HOST}/u/{os.getenv("USER_LOGIN")}/friends"
    MESSAGES_PAGE = f"{HOST}/messages/all"