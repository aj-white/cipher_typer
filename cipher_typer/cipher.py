"""
This contains 2 classes which implement encryption slightly differently.
Both classes allow the base cipher to be selected from one or all of:
    lowercase, uppercase letters, numbers, punctutation (minus \ and ") and whitespace
By default the most secure of 'all' is selected

CaeserCipher is a classic caeser cipher which shifts characters according to a given key
CaeserSeedCipher is a modified cipher that is more a substitution cipher than a caeser cipher.
Instead of shifting characters by a key it creates a random character map, randomness is controlled
by the random.seed() method to enable decryption
"""

import random
import string


class InvalidSelector(Exception):
    pass


class CaeserCipher:
    """Class to represent caeser cipher that allows use of numbers, punctuation and spaces

    Args:
        selector: selects which set of characters to include in cipher
                  Examples:
                      "lower": include only lower case characters
                      "upper": include only upper case characters
                      "both": includes lower and upper case characters
                      "all": includes lower case, upper case, punctuation, numbers and whitespace characters
    """

    CHARACTERS = (
        string.ascii_lowercase,
        string.ascii_uppercase,
        # Remove backslash to avoid escape character issues and quote mark to avoid string interpretation issues
        "".join(i for i in string.punctuation if i not in ["\\", '"']),
        string.digits,
        " ",
    )

    def __init__(self, selector="all"):
        """Setup class instance by choosing which characters to include in cipher"""

        self.characters = self._get_characters(selector)
        self.max_key_length = len(self.characters)
        self.translated = ""

    def _get_characters(self, selector: str):
        if selector == "lower":
            return CaeserCipher.CHARACTERS[0]
        elif selector == "upper":
            return CaeserCipher.CHARACTERS[1]
        elif selector == "both":
            return "".join(CaeserCipher.CHARACTERS[i] for i in [0, 1])
        elif selector == "all":
            return "".join(CaeserCipher.CHARACTERS[i] for i in [0, 1, 2, 3, 4])
        else:
            raise InvalidSelector("Selector options: lower, upper, both, all")

    def _crypto(self, mode: str) -> str:
        for char in self.message:
            if char in self.characters:
                char_index = self.characters.find(char)

                if mode == "encrypt":
                    char_index += self.key
                elif mode == "decrypt":
                    char_index -= self.key

                if char_index >= self.max_key_length:
                    char_index -= self.max_key_length
                elif char_index < 0:
                    char_index += self.max_key_length

                self.translated += self.characters[char_index]
            else:
                self.translated += char

        return self.translated

    def encrypt(self, message: str, key: int = 0) -> str:
        if key > self.max_key_length:
            raise IndexError(f"key must be less than {self.max_key_length}")
        self.translated = ""
        self.key = key
        self.message = message
        return self._crypto("encrypt")

    def decrypt(self, message: str, key: int = 0) -> str:
        if key > self.max_key_length:
            raise IndexError(f"key must be less than {self.max_key_length}")
        self.translated = ""
        self.key = key
        self.message = message
        return self._crypto("decrypt")


class CaeserSeedCipher:
    """Class to represent caeser cipher that allows use of numbers, punctuation and spaces

    Args:
        selector: selects which set of characters to include in cipher
                Examples:
                    "lower": include only lower case characters
                    "upper": include only upper case characters
                    "both": includes lower and upper case characters
                    "all": includes lower case, upper case, punctuation, numbers and whitespace characters
    """

    CHARACTERS = (
        string.ascii_lowercase,
        string.ascii_uppercase,
        # Remove backslash to avoid escape character issues and quote mark to avoid string interpretation issues
        "".join(i for i in string.punctuation if i not in ["\\", '"']),
        string.digits,
        " ",
    )

    def __init__(self, selector="all"):
        """Setup class instance by choosing which characters to include in cipher"""

        self.characters = self._get_characters(selector)
        self.max_key_length = len(self.characters)
        self.translated = ""

    def _get_characters(self, selector: str):
        if selector == "lower":
            return CaeserSeedCipher.CHARACTERS[0]
        elif selector == "upper":
            return CaeserSeedCipher.CHARACTERS[1]
        elif selector == "both":
            return "".join(CaeserSeedCipher.CHARACTERS[i] for i in [0, 1])
        elif selector == "all":
            return "".join(CaeserSeedCipher.CHARACTERS[i] for i in [0, 1, 2, 3, 4])
        else:
            raise InvalidSelector("Selector options: lower, upper, both, all")

    def _crypto(self, mode: str) -> str:
        random.seed(self.key)
        cipher = "".join(random.sample(self.characters, self.max_key_length))
        for char in self.message:
            if char in self.characters:
                if mode == "encrypt":
                    char_map = dict(zip(self.characters, cipher))
                    self.translated += char_map[char]
                elif mode == "decrypt":
                    char_map = dict(zip(cipher, self.characters))
                    self.translated += char_map[char]
            else:
                self.translated += char

        return self.translated

    def encrypt(self, message: str, key: int = 0) -> str:
        self.translated = ""
        self.key = key
        self.message = message
        return self._crypto("encrypt")

    def decrypt(self, message: str, key: int = 0) -> str:
        self.translated = ""
        self.key = key
        self.message = message
        return self._crypto("decrypt")


if __name__ == "__main__":
    print("Using CaeserCipher:")
    cipher = CaeserCipher()
    print(cipher.encrypt("Secret message.", 13))
    print(cipher.decrypt("'rpErGmzrFFntr`", 13))
    print(cipher.encrypt("John Doe will be on the [08:00] train @King's Cross", 56))
    print(cipher.decrypt("9>-=%3>*%{.;;%'*%>=%^-*%KT#DTTL%^[&.=%J .=,u]%2[>]]", 56))

    print("\nUsing CaeserSeedCipher:")
    c = CaeserSeedCipher()
    print(c.encrypt("Secret message.", 13))
    print(c.decrypt("hx5dx}fqx%%HDx-", 13))
    print(c.encrypt("John Doe will be on the [08:00] train @King's Cross", 56))
    print(c.decrypt("lG#R27G:2rD||2b:2GR2_#:29uEzuu%2_c?DR2BTDR=,`2xcG``", 56))
