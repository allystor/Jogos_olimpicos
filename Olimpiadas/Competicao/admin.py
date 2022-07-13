from django.contrib import admin

# Register your models here.

from .models import Competicao, Atleta

admin.site.register(Competicao)

admin.site.register(Atleta)
