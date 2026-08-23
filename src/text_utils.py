"""Small text helpers used across the playground scripts."""

import re
import unicodedata

_SLUG_SEPARATOR = re.compile(r"[^a-z0-9]+")


def slugify(value: str) -> str:
    """Turn arbitrary text into a URL-safe slug."""
    normalized = unicodedata.normalize("NFKD", value)
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return _SLUG_SEPARATOR.sub("-", ascii_only).strip("-")


def truncate(value: str, limit: int, suffix: str = "...") -> str:
    """Shorten text to `limit` characters, keeping whole words where possible."""
    if limit <= 0:
        raise ValueError("limit must be positive")
    if len(value) <= limit:
        return value
    cut = value[: limit - len(suffix)].rstrip()
    head, sep, _ = cut.rpartition(" ")
    return (head if sep else cut) + suffix
