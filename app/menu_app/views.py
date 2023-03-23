from django.shortcuts import render


def home(request, url=None):
    return render(request, 'menu_app/index.html')
