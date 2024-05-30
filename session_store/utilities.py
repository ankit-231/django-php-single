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
    print(session, "session")
    today = datetime.datetime.now()
    print(session.expire_date, today)

    is_expired = session.expire_date < today
    if is_expired:
        return None
    print(is_expired)
    user_id = session.user_id if session else None

    user = Users.objects.filter().last() if user_id else None

    return user


class Auth:

    def get_app_key():
        key = config("APP_KEY")
        if not key:
            raise ValueError("APP_KEY not configured properly")
        return key

    def _byte(string: str):
        return string.encode("utf-8")

    @classmethod
    def create_hash(cls, password):
        _password = cls._byte(password)
        salt = cls.get_app_key()
        hashed = bcrypt.hashpw(_password, salt)
        return hashed

    @classmethod
    def check_password(cls, user: Users, password: str):
        hashed = cls.create_hash(password)
        return bcrypt.checkpw(password, hashed)

    @classmethod
    def set_password(cls, user: Users, password: str):
        hashed = cls.create_hash(password)
        user.password = hashed
        # user.save()


def get_is_authenticated(request):
    print(request.user, "heheh")
    if request.user:
        if isinstance(request.user, Users):
            return True

    return False


def hash_password_bcrypt(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password
