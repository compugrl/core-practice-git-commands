import pytest


def always_returns_true():
    return True
    print(f"Shayla was here!")
    print(f"Shayla was here again!")


def test_always_returns_true():
    assert always_returns_true()
