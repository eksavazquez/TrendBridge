import logging
import time
from dotenv import load_dotenv
from trendbridge.auth import get_bluesky_client, get_twitter_client
from trendbridge.browser import get_most_relevant_tweet
from trendbridge.post import create_post

logger = logging.getLogger(__name__)

CitiesMAP: dict[str, int] = {
    "Madrid": 766273,
    "Barcelona": 753692,
    "Valencia": 776688,
    "Sevilla": 774508,
    "Palma": 769293,
}

Cities = [
    "Madrid",
    "Barcelona",
    "Valencia",
    "Sevilla",
    "Palma",
]

load_dotenv()

logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    datefmt="%Y-%m-%d %H:%M:%S",  # Date format
)


def bot_process(city="Madrid"):
    bluesky_client, _ = get_bluesky_client()
    twitter_client = get_twitter_client()

    try:
        most_relevant_tweet = get_most_relevant_tweet(twitter_client, CitiesMAP[city])
    except Exception as e:
        logger.error(f"Error getting most relevant tweet: {e}")
        return
    print(most_relevant_tweet)
    author_id = most_relevant_tweet["author_id"]
    print("Author ID: ", author_id)
    # Get the user's profile

    try:
        user = twitter_client.get_user(id=author_id, user_auth=True)
        username = user.data["username"]
    except Exception as e:
        username = None
    print("User: ", username)
    post = create_post(most_relevant_tweet["text"], username)
    print("Post to send: ", post)
    bluesky_client.send_post(post)


if __name__ == "__main__":
    i = 0
    while True:
        bot_process(Cities[i])
        i = (i + 1) % len(Cities)
        print("Sleeping for 1 day...")
        time.sleep(86400)
