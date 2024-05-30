from django.contrib.sessions.backends.db import SessionStore as DbSessionStore
from core.models import Sessions
from django.utils import timezone

class SessionStore(DbSessionStore):
    @classmethod
    def get_model_class(cls):
        # Avoids a circular import and allows importing SessionStore when
        # django.contrib.sessions is not in INSTALLED_APPS.
        # from django.contrib.sessions.models import Session
        from core.models import Sessions

        return Sessions

    # pass

# class CustomSessionStore(DbSessionStore):

#     @classmethod
#     def get_model_class(cls):
#         return Sessions

#     def create_model_instance(self, data):
#         # Map Django's session fields to your custom columns
#         return Sessions(
#             session_key=data["session_key"],
#             session_data=data["session_data"],
#             expire_date=data["expire_date"],
#         )

#     def load(self):
#         try:
#             s = Sessions.objects.get(
#                 session_key=self.session_key, expire_date__gt=timezone.now()
#             )
#             return self.decode(s.session_data)
#         except Sessions.DoesNotExist:
#             self.create()
#             return {}

#     def save(self, must_create=False):
#         if must_create:
#             self.create()
#         else:
#             obj, created = Sessions.objects.update_or_create(
#                 session_key=self.session_key,
#                 defaults={
#                     "session_data": self.encode(self._get_session(no_load=must_create)),
#                     "expire_date": self.get_expiry_date(),
#                 },
#             )
#             if created:
#                 self._session_key = obj.session_key
