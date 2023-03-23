from django.urls import path

from .views import home

urlpatterns = [
    path('', home, name='index'),
    path('<slug:url>/', home, name='index'),
]
