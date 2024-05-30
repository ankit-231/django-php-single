from core.models import Sessions, Users
import datetime
from django.conf import settings


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
