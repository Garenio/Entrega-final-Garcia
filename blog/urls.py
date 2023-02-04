from django.urls import path

from blog.views import (
    ReviewCreateView
)


urlpatterns = [
    path('agregar-review/', ReviewCreateView.as_view(), name= 'agregar_review'),
]