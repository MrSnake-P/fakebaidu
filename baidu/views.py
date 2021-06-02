from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == "POST":
        account = request.POST.get("account")
        password = request.POST.get("password")
        user_dict = {
            "account": account,
            "password": password
        }
        print(user_dict)
    return render(request, "index.html")


