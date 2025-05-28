from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'phone', 'status')
    search_fields = ('nom', 'email')
    list_filter = ('status',)

