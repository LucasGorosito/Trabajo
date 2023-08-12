from django.contrib import admin
from .models import Chaco, Corrientes, Formosa, Total

# Register your models here.
admin.site.register(Chaco)
admin.site.register(Corrientes)
admin.site.register(Formosa)
admin.site.register(Total)