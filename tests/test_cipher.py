import string

import pytest
from cipher_typer.cipher import CaeserCipher, CaeserSeedCipher


def test_caeser_no_key():
    c = CaeserCipher()
    message = string.ascii_letters + string.digits
    enc = c.encrypt(message)
    dec = c.decrypt(enc)
    assert dec == message


def test_caeser_cipher():
    c = CaeserCipher()
    message = string.ascii_letters + string.digits
    enc = c.encrypt(message, 25)
    dec = c.decrypt(enc, 25)
    assert dec == message


def test_caeser_key_error():
    c = CaeserCipher()
    message = string.ascii_lowercase
    with pytest.raises(IndexError):
        assert c.encrypt(message, 95)
        assert c.decrypt(message, 98)


# Test CaserSeedCipher class
def test_caeser_seed_no_key():
    cs = CaeserSeedCipher()
    message = string.ascii_letters + string.digits
    enc = cs.encrypt(message)
    dec = cs.decrypt(enc)
    assert dec == message


def test_caeser_seed():
    cs = CaeserSeedCipher()
    message = string.ascii_letters + " " + string.digits + "#"
    enc = cs.encrypt(message, 60)
    dec = cs.decrypt(enc, 60)
    assert dec == message


def test_caeser_seed_key_error():
    cs = CaeserSeedCipher()
    with pytest.raises(IndexError):
        assert cs.encrypt("Jeff", 100)
        assert cs.decrypt("Jeff", 230)
