"""Rotas principais: página inicial, enquetes e painel administrativo."""
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import include, path


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='polls:index', permanent=False), name='home'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
