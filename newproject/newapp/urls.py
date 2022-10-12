"""Ecommerce_API_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import *
from newapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
# path('categories', views.ListCategory.as_view()),
# path('categories/<int:pk>/', DetailCategory.as_view()),
# path('products', ListProduct.as_view()),
path('products/', urlauto_call),
path('homepage/', views.home_page),
path('delete/', views.deleteafterweek.as_view()),
path('url/scrp/data/', productlist.as_view()),
path('url/', views.url_view),


]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)