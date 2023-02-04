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
from blog.forms import ReviewFormulario, ReviewUpdateForm

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review 
    form_class = ReviewFormulario
    success_url = reverse_lazy('reviews')
    template_name = 'blog/agregar_review.html'

def listar_reviews(request):
    contexto = {
        'reviews': Review.objects.all()
    }
    return render(
        request=request,
        template_name='blog/reviews.html',
        context=contexto,
    )

def buscar_reviews(request):
    if request.method == "POST":
        data = request.POST
        reviews = Review.objects.filter(
            Q(titulo__contains=data['busqueda']) | Q(autor__contains=data['busqueda'])
        )
        contexto = {
            'reviews': reviews
        }
        return render(
            request=request,
            template_name='blog/reviews.html',
            context=contexto,
        )

class ReviewDetailView(DetailView):
    model = Review
    success_url = reverse_lazy('reviews')
    template_name = "blog/detalle_review.html"

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review 
    form_class = ReviewUpdateForm
    success_url = reverse_lazy('reviews')
    template_name = 'blog/editar_review.html'

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('reviews')
    template_name = "blog/eliminar_review.html"