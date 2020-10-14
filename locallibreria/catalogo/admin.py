from django.contrib import admin
from . models import Formulario, Pasteles, User


# Register your models here.
admin.site.register(Formulario)
admin.site.register(Pasteles)
admin.site.register(User)