import os
from dotenv import load_dotenv

load_dotenv()


class Links:

    HOST = "https://demo.opensource-socialnetwork.org"

    user = os.getenv("USER_LOGIN")
    admin = os.getenv("ADMIN_LOGIN")

    LOGIN_PAGE = f"{HOST}/login"
    NEWS_FEED_PAGE = f"{HOST}/home"
    MESSAGES_PAGE = f"{HOST}/messages/all"

    FRIENDS_PAGE_USER = f"{HOST}/u/{user}/friends"
    FRIENDS_PAGE_ADMIN = f"{HOST}/u/{admin}/friends"