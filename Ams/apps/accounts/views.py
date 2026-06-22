from django.shortcuts import render

# Create your views here.
def login(request):
    print("Rendering login page")
    return render(request, 'accounts/login.html')

def signup(request):
    print("Rendering signup page")
    print("Request method:", request.method)
    # print(render(request, 'signup.html'))
    return render(request, "accounts/signup.html")