from datetime import datetime, timezone

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Review
from blog.forms import ReviewFormulario

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review 
    form_class = ReviewFormulario
    success_url = reverse_lazy('home')
    template_name = 'blog/agregar_review.html'

def reviews_home(request):
    reviews = Review.objects.all().order_by('-fecha_publicacion')[:4]
    return render(request, 'home.html', {'reviews': reviews})