from jose import jwt
from datetime import datetime, timedelta, UTC


class JWTAuthenticator:
    def __init__(self, secret_key: str, access_token_expire_minutes: int = 30, algorithm: str = "HS256",
                 REFRESH_TOKEN_EXPIRE_DAYS: int = 7):
        """
        Initialize the JWTAuthenticator with configurable parameters.

        Args:
            secret_key (str): The secret key used for signing JWT tokens.
            access_token_expire_minutes (int): The expiration time for access tokens in minutes.
            algorithm (str): The algorithm used for signing JWT tokens.
        """
        self.secret_key = secret_key
        self.access_token_expire_minutes = access_token_expire_minutes
        self.algorithm = algorithm
        self.REFRESH_TOKEN_EXPIRE_DAYS = REFRESH_TOKEN_EXPIRE_DAYS

    def create_access_token(self, user_info: dict) -> str:
        """
        Create a new JWT access token.

        Args:
            user_info (dict): The user Info.

        Returns:
            str: The JWT access token.
        """
        # Calculate token expiration time
        expires_delta = timedelta(minutes=self.access_token_expire_minutes)
        expire = datetime.now(UTC) + expires_delta

        # Create token payload
        __token_payload = {"sub": str(user_info.get('id')), "exp": expire}
        __token_payload.update(user_info)

        # Generate JWT access token
        __access_token = jwt.encode(__token_payload, self.secret_key, algorithm=self.algorithm)
        return __access_token

    def create_refresh_token(self, user_info: dict) -> str:
        """
        Create a new refresh token.

        Args:
            user_info (dict): The user ID.

        Returns:
            str: The refresh token.
        """
        expires_delta = timedelta(days=self.REFRESH_TOKEN_EXPIRE_DAYS)
        expire = datetime.now(UTC) + expires_delta
        refresh_token_payload = {"sub": str(user_info.get('id')), "exp": expire}
        refresh_token_payload.update(user_info)
        __refresh_token = jwt.encode(refresh_token_payload, self.secret_key, algorithm="HS256")
        return __refresh_token

    def verify_access_token(self, token: str) -> dict:
        """
        Verify and decode the JWT access token.

        Args:
            token (str): The JWT access token to verify.

        Returns:
            dict: The decoded token payload.
        """
        try:
            # Decode JWT access token
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            # Token has expired
            return {"error": "Token has expired"}
        except jwt.JWTError as e:
            # Token is invalid
            return {"error": f"Invalid token, {e}"}

    def refresh_tokens(self, refresh_token: str) -> dict:
        """
        Refresh access and refresh tokens.

        Args:
            refresh_token (str): The refresh token.

        Returns:
            dict: Dictionary containing new access and refresh tokens.
        """
        try:
            # Decode the refresh token to extract user information
            decoded_token = jwt.decode(refresh_token, self.secret_key, algorithms=[self.algorithm])
            user_info = decoded_token

            # Generate new access and refresh tokens
            new_access_token = self.create_access_token(user_info)
            new_refresh_token = self.create_refresh_token(user_info)

            return {"access_token": new_access_token, "refresh_token": new_refresh_token}
        except jwt.ExpiredSignatureError:
            # Handle expired token
            raise Exception("Refresh token has expired")
        except jwt.JWTError:
            # Handle invalid token
            raise Exception("Invalid refresh token")

    def create_tokens(self, user_info: dict) -> dict:
        """
        create access_token and refresh_token from user info.
        :param user_info:
        :return: (dict)
        """
        access_token = self.create_access_token(user_info)
        refresh_token = self.create_refresh_token(user_info)
        return {"access_token": access_token, "refresh_token": refresh_token}


if __name__ == '__main__':
    authenticator = JWTAuthenticator(secret_key="your-secret-key", access_token_expire_minutes=30, algorithm="HS256")
    _user_info = {"id": 123, "email_service": "test@test.com", "role": "admin"}
    _access_token = authenticator.create_access_token(user_info=_user_info)
    _refresh_token = authenticator.create_refresh_token(user_info=_user_info)
    print("Access Token:", _access_token)
    print("Refresh Token:", _refresh_token)
    token_payload = authenticator.verify_access_token(_access_token)
    _refresh_payload = authenticator.verify_access_token(_refresh_token)
    print("Token Payload:", token_payload)
    print("Refresh Payload:", _refresh_payload)
