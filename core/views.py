from django.shortcuts import render
from django.views import View
from core.models import Users
from django.contrib.auth.decorators import login_required

# from django.contrib.auth import authenticate

# Create your views here.

@login_required(login_url="login")
def index(request):
    # user = authenticate(request, username="admin", password="admin")
    # print(user)
    # print(request.user)
    resp = render(request, "index.html", context={"request": request})
    users = Users.objects.all()
    # print(users)
    # print(request.session)
    resp.set_cookie("test", "test", httponly=True)
    # resp.cookies
    resp.set_cookie("laravel_session", "4c0811115a1c50f26b5fc8671904cf7c6b5975a1")
    print(request.COOKIES)
    return resp


class ContactView(View):
    permission_required = "users.view_users"
    def get(self, request):
        return render(request, "contact.html")

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class MyView(LoginRequiredMixin, TemplateView):
    template_name = 'my_template.html'
    login_url = '/custom_login/'  # Optional customization