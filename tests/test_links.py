from trendbridge.post import detect_link


def test_detect_link():
    assert detect_link("https://example.com") is True
    assert detect_link("http://example.com") is True
    assert detect_link("www.example.com") is True
