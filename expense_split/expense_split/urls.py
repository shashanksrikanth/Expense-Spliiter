"""expense_split URL Configuration

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
from django.urls import path
from groups.api_views import GroupList, GroupCreate
from groups.views import create_group, email_group, delete_group, homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('api/v1/groups', GroupList.as_view()),
    path('api/v1/create', GroupCreate.as_view()),
    path('create_group/', create_group, name='create_group'),
    path('email_group/', email_group, name='email_group'),
    path('delete_group/', delete_group, name='delete_group')
]
