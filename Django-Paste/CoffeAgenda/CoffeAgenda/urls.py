"""CoffeAgenda URL Configuration

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
from cofe import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Coffe/', views.lista_eventos),
    path('Coffe/Lista', views.lista),
    path('Coffe/MakeCoffe/', views.create),
    path('Coffe/MakeCoffe/submit', views.submit_evento),
    path('Coffe/delete/<int:id_evento>', views.delete_evento),
    path('', RedirectView.as_view(url='/Coffe/')),
    path('login', views.login_users),
    path('submit', views.submit_users),
    path('logout/', views.tchau_user)
]
