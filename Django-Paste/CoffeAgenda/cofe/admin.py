from django.contrib import admin
from cofe.models import Envento
# Register your models here.

class EnventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','date_event','usuario_id')

admin.site.register(Envento, EnventoAdmin)