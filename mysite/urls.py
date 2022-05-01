"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', views.index, name='index'),
    path('about-us/', views.aboutus, name='about-us'),
    path('contact-us/', views.contactus, name='contact-us'),
    path('privacy-policy/', views.privacypolicy, name='privacy-policy'),
    path('testpage/', views.testpage, name='testpage'),
    # Job Posts related URLs
    path('job/categories', views.jobcategories, name='job-categories'),
    path('job/categories/<slug:url>', views.jobcategorypost, name='job-category-post'),
    path('job/categories/post/<slug:url>', views.singlejobpost, name='single-job-post'),
    # path('category/<slug:url>', views.category),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)