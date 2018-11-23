from django.contrib import admin

from .models import Cliente
from .models import Fornecedor

admin.site.register(Cliente)
admin.site.register(Fornecedor)