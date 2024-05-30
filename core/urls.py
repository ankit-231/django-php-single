from django.urls import path
from core import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("contact", view=views.ContactView.as_view(), name="contact"),
    path("contact/", view=views.ContactView.as_view(), name="contact"),
    # path("index", view=views.index, name="index"),
]
