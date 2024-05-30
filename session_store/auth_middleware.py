from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import SimpleLazyObject
from functools import partial

from session_store.utilities import get_user_from_session_key
from core.models import Sessions, Users


def get_user(request):
    if not hasattr(request, "_cached_user"):
        request._cached_user = auth.get_user(request)
    return request._cached_user


async def auser(request):
    if not hasattr(request, "_acached_user"):
        request._acached_user = await auth.aget_user(request)
    return request._acached_user


class CustomAnonymousUser:
    id = None
    pk = None
    username = ""
    is_staff = False
    is_active = False
    is_superuser = False
    # _groups = EmptyManager(Group)
    # _user_permissions = EmptyManager(Permission)

    def __str__(self):
        return "AnonymousUser"

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __hash__(self):
        return 1  # instances always return the same hash value

    def __int__(self):
        raise TypeError(
            "Cannot cast AnonymousUser to int. Are you trying to use it in place of "
            "User?"
        )

    def save(self):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    def delete(self):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    def set_password(self, raw_password):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    def check_password(self, raw_password):
        raise NotImplementedError(
            "Django doesn't provide a DB representation for AnonymousUser."
        )

    @property
    def groups(self):
        return self._groups

    @property
    def user_permissions(self):
        return self._user_permissions

    # def get_user_permissions(self, obj=None):
    #     return _user_get_permissions(self, obj, "user")

    # def get_group_permissions(self, obj=None):
    #     return set()

    # def get_all_permissions(self, obj=None):
    #     return _user_get_permissions(self, obj, "all")

    # def has_perm(self, perm, obj=None):
    #     return _user_has_perm(self, perm, obj=obj)

    # def has_perms(self, perm_list, obj=None):
    #     if not is_iterable(perm_list) or isinstance(perm_list, str):
    #         raise ValueError("perm_list must be an iterable of permissions.")
    #     return all(self.has_perm(perm, obj) for perm in perm_list)

    # def has_module_perms(self, module):
    #     return _user_has_module_perms(self, module)

    @property
    def is_anonymous(self):
        return True

    @property
    def is_authenticated(self):
        return False

    def get_username(self):
        return self.username


# class AuthenticationMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         print("of course")
#         user = get_user_from_session_key(request)

#         print(user, "ssssssss")

#         request.user = user if user else CustomAnonymousUser
#         # if not hasattr(request, "session"):
#         #     raise ImproperlyConfigured(
#         #         "The Django authentication middleware requires session "
#         #         "middleware to be installed. Edit your MIDDLEWARE setting to "
#         #         "insert "
#         #         "'django.contrib.sessions.middleware.SessionMiddleware' before "
#         #         "'django.contrib.auth.middleware.AuthenticationMiddleware'."
#         #     )
#         # request.user = SimpleLazyObject(lambda: get_user(request))
#         # request.auser = partial(auser, request)
#         # print(request.user)


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not hasattr(request, "session"):
            raise ImproperlyConfigured(
                """
                Create a custom session middleware or use the default middleware. Anyway provide session property to request before this middleware is run
                """
            )
        # print("of course")
        user = get_user_from_session_key(request)

        # print(user, "ssssssss")

        request.user = user if user else CustomAnonymousUser
