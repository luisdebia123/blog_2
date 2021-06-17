from django.contrib import admin
from .models import Entradas


# Register your models here.


class EntraAdminManager(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Entradas, EntraAdminManager)