from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutUs.as_view(), name='about'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('equipmentList/', include('equipmentList.urls')),
    path('equipmentMaintenance/', include('equipmentMaintenance.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
