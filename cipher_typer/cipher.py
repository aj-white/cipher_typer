"""
This contains 2 classes which implement encryption slightly differently.
Both classes allow the base cipher to be lowercase, uppercase letters, numbers,
punctutation (minus backslash and double quotes) and whitespace

CaeserCipher is a classic caeser cipher which shifts characters according to a given key
CaeserSeedCipher is a modified cipher that is more a substitution cipher than a caeser cipher.
Instead of shifting characters by a key it creates a random character map, randomness is controlled
by the random.seed() method to enable decryption
"""

import random
import string


class CaeserCipher:
    """Class to represent caeser cipher that allows use of numbers, punctuation and spaces"""

    CHARACTERS = (
        string.ascii_letters
        # Remove backslash to avoid escape character issues and quote mark to avoid string interpretation issues
        + "".join(i for i in string.punctuation if i not in ["\\", '"'])
        + string.digits
        + " "
    )

    def __init__(self):
        """Setup class instance characters for cipher"""

        self.characters = CaeserCipher.CHARACTERS
        self.max_key_length = len(self.characters)
        self.translated = ""

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
    """Class to represent caeser cipher that allows use of numbers, punctuation and spaces"""

    CHARACTERS = (
        string.ascii_letters
        # Remove backslash to avoid escape character issues and quote mark to avoid string interpretation issues
        + "".join(i for i in string.punctuation if i not in ["\\", '"'])
        + string.digits
        + " "
    )

    def __init__(self):
        """Setup class instance by choosing which characters to include in cipher"""

        self.characters = CaeserSeedCipher.CHARACTERS
        self.max_key_length = len(self.characters)
        self.translated = ""

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


if __name__ == "__main__":
    c = CaeserCipher()
    print(c.characters)
    print(c.max_key_length)
