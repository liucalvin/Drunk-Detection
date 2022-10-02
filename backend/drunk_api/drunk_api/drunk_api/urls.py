"""drunk_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from drunk_api.drunkapp import views

router = routers.DefaultRouter()

urlpatterns = [
    path('api/submit/', views.SubmitImage.as_view(), name="submit"),
    path('api/check_drunk/', views.CheckDrunk.as_view(), name="check_drunk"),
    path('api/ping/', views.Pong.as_view(), name="ping"),
]
