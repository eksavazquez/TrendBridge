import os
from atproto import Client
from atproto_client.models.app.bsky.actor.defs import ProfileViewDetailed
import tweepy


BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")


def get_twitter_client() -> tweepy.Client:
    """Get twitter client."""
    return tweepy.Client(
        consumer_key=os.getenv("X_CONSUMER_KEY"),
        consumer_secret=os.getenv("X_CONSUMER_SECRET"),
        access_token=os.getenv("X_ACCESS_TOKEN"),
        access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET"),
    )


def get_bluesky_client() -> Client | tuple[Client, ProfileViewDetailed]:
    """Get bluesky client."""
    bluesky_client = Client()
    profile = bluesky_client.login(
        os.getenv("BLUESKY_USERNAME"), os.getenv("BLUESKY_PASSWORD")
    )
    return bluesky_client, profile
