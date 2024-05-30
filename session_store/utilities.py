from core.models import Sessions, Users
import datetime
from django.conf import settings
import bcrypt
from decouple import config


def get_user_from_session_key(request):
    """
    returns User or None from the user_id in the session table
    """
    cookie_name = settings.SESSION_COOKIE_NAME or "laravel_session"
    session_id = request.COOKIES.get(cookie_name)
    session = (
        Sessions.objects.filter(session_key=session_id).last() if session_id else None
    )
    # print(session, "session")
    today = datetime.datetime.now()
    # print(session.expire_date, today)

    is_expired = session.expire_date < today
    if is_expired:
        return None
    # print(is_expired)
    user_id = session.user_id if session else None

    user = Users.objects.filter().last() if user_id else None

    return user


class Auth:

    def get_app_key():
        key = config("APP_KEY")
        if not key:
            raise ValueError("APP_KEY not configured properly")
        return key

    @classmethod
    def byte_password(cls, password: str):
        return password.encode("utf-8")

    @classmethod
    def create_hash(cls, password: str):
        salt = bcrypt.gensalt()
        to_byte = cls.byte_password(password)
        hashed = bcrypt.hashpw(to_byte, salt)
        return hashed

    @classmethod
    def check_password(cls, user: Users, password: str):
        user_password = user.password.encode("utf-8")
        # print(user_password, "utf-8utf-8")
        to_byte = cls.byte_password(password)
        return bcrypt.checkpw(to_byte, user_password)

    @classmethod
    def set_password(cls, user: Users, password: str):
        hashed = cls.create_hash(password)
        user.password = hashed
        # user.save()

    def authenticate(self, username: str, password: str):
        """
        returns Users or None
        """
        user = Users.objects.filter(username=username).last()
        if not user:
            return None

        password_match = self.check_password(user, password)

        if password_match:
            return user

        return None

    def login(self, user: Users):
        pass


def get_is_authenticated(request):
    # print(request.user, "heheh")
    if request.user:
        if isinstance(request.user, Users):
            return True

    return False


def hash_password_bcrypt(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    # Convert the hashed bytes to a string for storage
    final_hashed_password = hashed_password.decode('utf-8')
    db_hashcode = "$2y$10$A/23JxVIwCQKRZXWhxBddesw/QdczbFZ1buXhw8H/qR/pfDmpiHr."
    # print(bcrypt.checkpw(final_hashed_password, db_hashcode.encode('utf-8')))
    return final_hashed_password
