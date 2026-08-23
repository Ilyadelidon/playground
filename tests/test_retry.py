import pytest

from src.retry import retry


def test_returns_value_without_retrying():
    calls = []

    @retry(attempts=3, base_delay=0)
    def ok():
        calls.append(1)
        return "done"

    assert ok() == "done"
    assert len(calls) == 1


def test_retries_until_success():
    calls = []

    @retry(attempts=3, base_delay=0, jitter=0)
    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise ConnectionError("boom")
        return "recovered"

    assert flaky() == "recovered"
    assert len(calls) == 3


def test_reraises_after_last_attempt():
    @retry(attempts=2, base_delay=0, jitter=0)
    def always_fails():
        raise TimeoutError("nope")

    with pytest.raises(TimeoutError):
        always_fails()


def test_rejects_zero_attempts():
    with pytest.raises(ValueError):
        retry(attempts=0)
