# from sqlalchemy import select, text
#
# from packages.auth.base_authenticator import BaseAuthenticator
# from test_project.domain.models.user import User
# from packages.auth.hashing import PasswordHasher
#
#
# class UsernamePasswordAuthenticator(BaseAuthenticator):
#
#     async def authenticate(self, *args, **kwargs) -> User:
#         if 'username' not in kwargs or 'password' not in kwargs:
#             raise ValueError("'username' or 'password' is missing.")
#         username = kwargs['username']
#         password = kwargs['password']
#
#         try:
#                 stmt = select(User).where(User.username == username)
#                 user = await self.session_db.scalar(stmt)
#                 if not user:
#                     raise Exception("Authorization failed!.")
#                 hasher = PasswordHasher()
#                 match = hasher.verify_password(password=password, hashed_pass=user.hashed_password)
#                 if not match:
#                     raise Exception("Authorization failed!.")
#                 return user
#         except:
#                 raise
