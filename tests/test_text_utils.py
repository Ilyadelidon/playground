from src.text_utils import slugify, truncate


def test_slugify_strips_punctuation_and_case():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_handles_accents():
    assert slugify("Café Déjà Vu") == "cafe-deja-vu"


def test_truncate_keeps_short_strings():
    assert truncate("short", 10) == "short"


def test_truncate_breaks_on_word_boundary():
    assert truncate("the quick brown fox", 12) == "the quick..."
