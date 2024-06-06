from django.shortcuts import render
from django.http import JsonResponse
from .forms import URLForm
from .utils.header_scanner import scan_headers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .models import Scans

# def index(request):

#     # Authenticated users view their inbox
#     if request.user.is_authenticated:
#         return render(request, "scanner/index.html")
    

#     # Everyone else is prompted to sign in
#     else:
#         return HttpResponseRedirect(reverse("login"))
# @csrf_exempt
# @login_required
# def scan(request):
#     if request.method == 'POST':
#         form = URLForm(request.POST)
#         if form.is_valid():
#             url = form.cleaned_data['url']
#             results = scan_headers(url)
#             return render(request, 'scanner/results.html', {'results': results, 'url': url})
#     else:
#         form = URLForm()
#     return render(request, 'scanner/results.html', {'form': form})
csrf_exempt
@login_required
def index(request):
    # Authenticated users can scan URLs
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = URLForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data['url']
                results = scan_headers(url)
                return render(request, 'scanner/results.html', {'results': results, 'url': url})
        else:
            form = URLForm()
        return render(request, 'scanner/index.html', {'form': form})
    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))
    
@login_required
def scan_results(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        results = scan_headers(url)
        return JsonResponse(results)
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "scanner/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "scanner/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "scanner/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "scanner/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "scanner/register.html")


# # Create your views here.
