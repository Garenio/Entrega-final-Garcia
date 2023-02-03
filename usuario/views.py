from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from usuario.models import Avatar
from usuario.forms import AvatarFormulario, UserUpdateForm, PasswordUpdateForm

@login_required
def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('perfil')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='usuario/formulario_avatar.html',
        context={'form': formulario},
        )

def perfil(request):
    return render(
        request=request,
        template_name='usuario/perfil.html',
        )

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('perfil')
    template_name = 'usuario/editar_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

class PasswordUpdateView(PasswordChangeView):
    form_class = PasswordUpdateForm
    template_name = 'usuario/cambiar_password.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'usuario/password_exitoso.html', {})