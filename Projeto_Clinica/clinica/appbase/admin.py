from django.contrib import admin
from .models import Endereco, Pessoa, Medico, Paciente

# Register your models here.

admin.site.register(Endereco)
admin.site.register(Pessoa)
admin.site.register(Medico)
admin.site.register(Paciente)
