from django.contrib import admin
from .models import Funcionario, Cliente


# Register your models here.
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo', 'departamento')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'nascimento', 'is_deleted')
    list_filter = ('is_deleted',)
    actions = ['restore_clients']

    def restore_clients(self, request, queryset):
        queryset.update(is_deleted=False)

    restore_clients.short_description = 'Restaurar clientes'

#admin.site.register(Funcionario)
