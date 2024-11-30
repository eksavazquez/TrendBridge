import os
import requests
import tweepy

MADRID_WOEID = 766273


def get_trending_topics(bearer_token, woeid=1):
    """
    Fetch trending topics for a given WOEID.
    """
    url = f"https://api.twitter.com/1.1/trends/place.json?id={woeid}"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        trends = response.json()[0]["trends"]
        return [trend["name"] for trend in trends]
    else:
        print(f"Error fetching trends: {response.status_code}, {response.text}")
        return []


def get_most_relevant_tweet_from_trend(
    trend: str,
    twitter_client: tweepy.Client,
    woeid: int = MADRID_WOEID,
) -> str | None:
    """Get most relevant tweet from trend."""
    tweets = twitter_client.search_recent_tweets(
        trend,
        sort_order="relevancy",
        expansions="author_id",
        user_auth=True,
    )
    first_tweet = tweets.data[0]
    return first_tweet


def get_most_relevant_tweet(
    twitter_client: tweepy.Client,
    woeid: int = MADRID_WOEID,
) -> str | None:
    """Get most relevant tweet."""
    trending_topics = get_trending_topics(os.getenv("USER_BEARER_TOKEN"), woeid)
    if trending_topics:
        first_trend = trending_topics[0]
        print("First trend: ", first_trend)
        return get_most_relevant_tweet_from_trend(first_trend, twitter_client, woeid)
    return None
