from .views import homePageView
from django.urls import path, include

urlpatterns = [
    path('', homePageView, name='home'),
    path('', include('homepage.urls')),
]