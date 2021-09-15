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
def test_caeser_seed_all_no_key():
    cs = CaeserSeedCipher()
    message = string.ascii_letters + string.digits
    enc = cs.encrypt(message)
    dec = cs.decrypt(enc)
    assert dec == message


def test_caeser_seed_all():
    cs = CaeserSeedCipher()
    message = string.ascii_letters + " " + string.digits + "#"
    enc = cs.encrypt(message, 60)
    dec = cs.decrypt(enc, 60)
    assert dec == message


def test_caeser_seed_lower():
    cs = CaeserSeedCipher("lower")
    message = string.ascii_lowercase
    enc = cs.encrypt(message, 3)
    dec = cs.decrypt(enc, 3)
    assert dec == message


def test_caeser_seed_upper():
    cs = CaeserSeedCipher("upper")
    message = string.ascii_uppercase
    enc = cs.encrypt(message, 11)
    dec = cs.decrypt(enc, 11)
    assert dec == message


def test_caeser_seed_both():
    cs = CaeserSeedCipher("both")
    message = string.ascii_letters
    enc = cs.encrypt(message, 12)
    dec = cs.decrypt(enc, 12)
    assert dec == message


def test_caeser_seed_key_error():
    cs = CaeserSeedCipher()
    with pytest.raises(IndexError):
        assert cs.encrypt("Jeff", 100)
        assert cs.decrypt("Jeff", 230)


def test_caeser_seed_invalid_selector():
    with pytest.raises(InvalidSelector):
        assert CaeserSeedCipher("poo")


def test_caser_seed_mixed_case_lower():
    cs = CaeserSeedCipher("lower")
    message = "I am in B8th CaseS"
    assert cs.encrypt(message, 7) == "I kq lp B8od CktbS"


def test_caser_seed_mixed_case_upper():
    cs = CaeserSeedCipher("upper")
    message = "&I am in UPper and LowerCASE WIth 67"
    assert cs.encrypt(message, 18) == "&S am in JMper and EowerVFCK XSth 67"
