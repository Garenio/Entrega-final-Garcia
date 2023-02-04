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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from tecnoreview.views import home, about
from registro.views import registro, login_view, CustomLogoutView
from blog.views import listar_reviews, buscar_reviews, ReviewDetailView

urlpatterns = [
    path('admin/', admin.site.urls),

    ## URLS GENERALES
    path('', home, name="home"),
    path('about/', about, name="about"),

    ## URLS REGISTRO
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),

    ## URLS USUARIOS
    path('usuario/', include('usuario.urls')),

    ## URLS REVIEWS
    path('reviews/', listar_reviews, name="reviews"),
    path('buscar-reviews/', buscar_reviews, name="buscar_reviews"),
    path('review/', include('blog.urls')),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name="detalle_review"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
