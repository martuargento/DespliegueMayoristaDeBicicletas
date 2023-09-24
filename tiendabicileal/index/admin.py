from django.contrib import admin
from .models import Bicicleta

# Register your models here.
admin.site.register(Bicicleta)

class Bicileal(admin.ModelAdmin):
    readonly_fields=('creado','actualizado')