import logging

from passlib.context import CryptContext


class PasswordHasher:
    def __init__(self, schemes=None, deprecated: str = "auto"):
        if schemes is None:
            schemes = ["bcrypt"]
        self.password_context = CryptContext(schemes=schemes, deprecated=deprecated)

    def get_hashed_password(self, password: str) -> str:
        """
        Hashes the provided password.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password.
        """
        return self.password_context.hash(password)

    def verify_password(self, password: str, hashed_pass: str) -> bool:
        """
        Verifies if the provided password matches the hashed password.

        Args:
            password (str): The password to verify.
            hashed_pass (str): The hashed password.

        Returns:
            bool: True if the password matches the hashed password, False otherwise.
        """
        return self.password_context.verify(password, hashed_pass)


if __name__ == '__main__':
    logging.getLogger('passlib').setLevel(logging.ERROR)
    hasher: PasswordHasher = PasswordHasher(schemes=["bcrypt"], deprecated="auto", )
    _password = hasher.get_hashed_password("password")
    print(_password)
    # verify_pass = hasher.verify_password("password", _password)
    # print(f"verified - {verify_pass}")
