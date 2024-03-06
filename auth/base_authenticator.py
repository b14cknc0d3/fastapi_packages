from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class BaseAuthenticator:
    def __init__(self, session_db: AsyncSession):
        """
        Initialize the BaseAuthenticator with a user database and JWT handler.

        Args:
            session_db: Session = Depends(SessionLocal).

        """
        self.session_db = session_db

    @abstractmethod
    async def authenticate(self, *args, **kwargs):
        """
        Authenticate a user.

        This method should be overridden by subclasses.

        Returns:
            UserSchema: user if authentication succeeds, None otherwise.
        """
        raise NotImplementedError("Subclasses must implement the authenticate method.")
