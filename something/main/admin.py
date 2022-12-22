from django.contrib import admin
from .models import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date',  'created')
    fieldsets = (
        ('Информация', {'fields': ('email', 'name', 'phone_number', 'object_name', 'date', 'field1', 'field2')}),
    )
    search_fields = ('email', )
    ordering = ("-created",)
