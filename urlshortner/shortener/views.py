from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
import string
import random

# Create your views here.
def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST['original_url']
        short_url = generate_short_url()
        URL.objects.create(original_url=original_url, short_url=short_url)
        return render(request, 'shortener/success.html', {'short_url': short_url})
    return render(request, 'shortener/index.html')

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)