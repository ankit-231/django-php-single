from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from session_store.utilities import get_user_from_session_key
from core.models import Users


class AuthenticationBackend(BaseBackend):
    """
    Authenticate against cookie's session_id
    """

    def authenticate(self, request):
        user = get_user_from_session_key(request)
        return user

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None
