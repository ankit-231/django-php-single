from django.shortcuts import render
from django.views import View
from core.models import Users

# from django.contrib.auth.decorators import login_required

from session_store.utilities import Auth

# from django.contrib.auth import authenticate
from django.contrib.auth import authenticate

from session_store.utilities import get_is_authenticated, hash_password_bcrypt

# Create your views here.


def index(request):
    # user = authenticate(request, username="admin", password="admin")
    # print(user)
    # print(request.user)
    user_data = "you are not authenticated"
    user_name = "anonymous user"
    if get_is_authenticated(request):
        user_data = "you are authenticated"
        user_name = request.user.name
        # print(user_name,"user_name")
        password = request.user.password
        print(password, "password")
    
    users = Users.objects.all()
    # print(users)
    # print(request.session)
    # resp.set_cookie("test", "test", httponly=True)
    # # resp.cookies
    # resp.set_cookie("laravel_session", "4c0811115a1c50f26b5fc8671904cf7c6b5975a1")
    print(request.COOKIES)
    password = "Minbhawan@44"
    user = Users.objects.get(id=3)
    auth = Auth
    is_ok = auth.check_password(user=user, password=password)
    print(is_ok, "hash")
    data_ = {"is_ok": is_ok}
    resp = render(
        request,
        "index.html",
        context={"request": request, "user_data": user_data, "user_name": user_name, "data": data_},
    )
    return resp


class ContactView(View):
    permission_required = "users.view_users"

    def post(self, request):
        if request.method == "POST":
            user_name = request.POST.get("username")
            password = request.POST.get("password")
            hashed_pass = hash_password_bcrypt(password)
            return render(
                request,
                "contact.html",
                context={"user_name": user_name, "password": hashed_pass},
            )
        else:
            return render(request, "contact.html", context={"error": "Sorry please"})


# class MyView(LoginRequiredMixin, TemplateView):
#     template_name = 'my_template.html'
#     login_url = '/custom_login/'  # Optional customization
