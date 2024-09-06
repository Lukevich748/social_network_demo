import os
from dotenv import load_dotenv

load_dotenv()


class Links:

    HOST = "https://demo.opensource-socialnetwork.org"

    LOGIN_PAGE = f"{HOST}/login"
    NEWS_FEED_PAGE = f"{HOST}/home"
    MESSAGES_PAGE = f"{HOST}/messages/all"
    FRIENDS_PAGE_USER = f"{HOST}/u/{os.getenv("USER_LOGIN")}/friends"
    FRIENDS_PAGE_ADMIN = f"{HOST}/u/{os.getenv("ADMIN_LOGIN")}/friends"