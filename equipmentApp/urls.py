from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutUs.as_view(), name='about'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
]
