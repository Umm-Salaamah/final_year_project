from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
from .forms import URLForm
from .utils.header_scanner import scan_headers
from .models import ScanResult, User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required
def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = URLForm(request.POST)
            if form.is_valid():
                url = form.cleaned_data['url']
                results = scan_headers(url)
                
                # Save scan results to the database
                scan_result = ScanResult(user=request.user, url=url, results=results)
                scan_result.save()
                
                return render(request, 'scanner/results.html', {'results': results, 'url': url})
        else:
            form = URLForm()
        return render(request, 'scanner/index.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse("login"))

@login_required
def scan_results(request, scan_id=None):
    if request.method == 'POST':
        url = request.POST.get('url')
        results = scan_headers(url)
        return JsonResponse(results)
    
    # Handle GET request to view a specific scan result
    if scan_id:
        scan = ScanResult.objects.get(id=scan_id, user=request.user)
        return render(request, 'scanner/results.html', {'results': scan.results, 'url': scan.url})
    
    # If no scan_id is provided, redirect to the previous scans page
    return redirect('previous_scans')

@login_required
def previous_scans(request):
    scans = ScanResult.objects.filter(user=request.user).order_by('-scanned_at')
    return render(request, 'scanner/previous_scans.html', {'scans': scans})

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "scanner/login.html", {"message": "Invalid email and/or password."})
    else:
        return render(request, "scanner/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "scanner/register.html", {"message": "Passwords must match."})

        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "scanner/register.html", {"message": "Email address already taken."})
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "scanner/register.html")
