from django.shortcuts import render
from django.http import JsonResponse
from .forms import URLForm
from .utils.header_scanner import scan_headers


def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            results = scan_headers(url)
            return render(request, 'scanner/results.html', {'results': results, 'url': url})
    else:
        form = URLForm()
    return render(request, 'scanner/index.html', {'form': form})

def scan_results(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        results = scan_headers(url)
        return JsonResponse(results)


# Create your views here.
