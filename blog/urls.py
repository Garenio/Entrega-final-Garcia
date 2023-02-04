from django.urls import path

from blog.views import (
    ReviewCreateView, ReviewUpdateView, ReviewDeleteView
)


urlpatterns = [
    path('agregar-review/', ReviewCreateView.as_view(), name= 'agregar_review'),
    path('modificar-review/<int:pk>/', ReviewUpdateView.as_view(), name= 'editar_review'),
    path('eliminar-review/<int:pk>/', ReviewDeleteView.as_view(), name="eliminar_review"),
]