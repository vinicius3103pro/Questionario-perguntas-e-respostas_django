from django.contrib import admin

# Disponibiliza perguntas e opções no painel administrativo.

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)