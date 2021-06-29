import string

import pytest
from cipher_typer.cipher import CaeserCipher, InvalidSelector


def test_caeser_all_no_key():
    c = CaeserCipher("all")
    message = string.ascii_letters + string.digits
    enc = c.encrypt(message)
    dec = c.decrypt(enc)
    assert dec == message


def test_caeser_all():
    c = CaeserCipher("all")
    message = string.ascii_letters + string.digits
    enc = c.encrypt(message, 25)
    dec = c.decrypt(enc, 25)
    assert dec == message


def test_caeser_lower():
    c = CaeserCipher("lower")
    message = string.ascii_lowercase
    enc = c.encrypt(message, 18)
    dec = c.decrypt(enc, 18)
    assert dec == message


def test_caeser_upper():
    c = CaeserCipher("upper")
    message = string.ascii_uppercase
    enc = c.encrypt(message, 13)
    dec = c.decrypt(enc, 13)
    assert dec == message


def test_caeser_both():
    c = CaeserCipher("both")
    message = "I am BOTH Upper and lowerCase"
    enc = c.encrypt(message, 9)
    dec = c.decrypt(enc, 9)
    assert dec == message


def test_caeser_key_error():
    c = CaeserCipher("lower")
    message = string.ascii_lowercase
    with pytest.raises(IndexError):
        assert c.encrypt(message, 56)


def test_caeser_invalid_selector():
    with pytest.raises(InvalidSelector):
        assert CaeserCipher("jeff")


def test_caeser_mixed_case_message_with_lower():
    c = CaeserCipher("lower")
    message = "I am in B8th CaseS"
    assert c.encrypt(message, 7) == "I ht pu B8ao ChzlS"


def test_caser_mixed_case_message_with_upper():
    c = CaeserCipher("upper")
    message = "&I am in UPper and LowerCASE WIth 67"
    assert c.encrypt(message, 18) == "&A am in MHper and DowerUSKW OAth 67"
