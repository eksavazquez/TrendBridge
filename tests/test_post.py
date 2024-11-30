import re
from trendbridge.post import create_post

LINK_PATTERN = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"


def test_create_post():
    text = (
        "¿a por quién vas? \n\n🔁 Óscar❤️ Violeta\n\n#GHGala13 https://t.co/4utVtdQolN"
    )
    post = create_post(text, "alvvazort")
    print(post)
