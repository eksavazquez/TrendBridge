import re

from atproto_client.utils import TextBuilder

from atproto import client_utils

LINK_PATTERN = r"https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}"

HASTAG_PATTERN = r"#[a-zA-Z0-9]+"

BOTH_PATTERNS = f"({LINK_PATTERN}|{HASTAG_PATTERN})"

def detect_link(text: str) -> bool:
    """Detect link."""
    return bool(re.match(LINK_PATTERN, text))


def create_post(
    text: str,
    username: str | None,
    link_pattern: str = LINK_PATTERN,
    *,
    city: str = "",
) -> str | TextBuilder:
    """Create post."""
    post = client_utils.TextBuilder()
    post.text(f"Popular en X {city} 🌟:")
    post.text("")
    steps = re.split(BOTH_PATTERNS, text)
    for step in steps:
        if re.match(f"({link_pattern})", step):
            post.link(step, step)
        elif re.match(f"({HASTAG_PATTERN})", step):
            post.link(step, f"https://x.com/search?q=%23{step[1:]}")
        else:
            post.text(step)
    post.text("\n")
    if username:
        post.text("By: ")
        post.link(f"{username}", f"https://x.com/{username}")
    return post
