"""proyecto_final URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from usuario.views import agregar_avatar, perfil, ProfileUpdateView, PasswordUpdateView, password_exitoso

urlpatterns = [
    path('editar-avatar/', agregar_avatar, name="agregar_avatar"),
    path('perfil/', perfil, name="perfil"),
    path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('cambiar-password/', PasswordUpdateView.as_view(), name="cambiar_password"),
    path('password-exitoso/', password_exitoso, name="password_exitoso"),
]