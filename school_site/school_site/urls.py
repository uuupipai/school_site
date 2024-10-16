"""school_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from .views import home_view
from django.contrib.auth import views as auth_views
from users import views as user_views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', home_view, name='home'),
    path('users/register/', user_views.register, name='register'),
    path('users/login/', user_views.login_view, name='login'),
    path('users/profile/', user_views.profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]

