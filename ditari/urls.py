"""ditari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from home import views as homeViews
from django.contrib.auth import views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lenda/',homeViews.register,name ='regjistro-lenden'),
    path('login/', userViews.LoginView.as_view(template_name = 'home/login.html'), name = 'login'),
    path('regjistroProfesorin/',homeViews.regjistroProfesorin, name='Regjistro-Profin'),
    path('regjistroKlasen/',homeViews.regjistroKlasen, name='regjistro-klasen'),
    path('regjistroNxenesin/',homeViews.regjistroNxenesin, name='Regjistro - nxenesin'),
    path('regjistroNoten/',homeViews.regjistroNoten, name='regjistro-noten'),
    path('regjistroMungesen/',homeViews.regjistroMungesen, name='regjistro-mungesen'),
    path('regjistroOrenMesimore/',homeViews.regjistroOrenMesimore, name='regjistro-oren-mesimore'),
    path('logout/', userViews.LogoutView.as_view(template_name = 'home/logout.html'), name = 'logout'),
]
