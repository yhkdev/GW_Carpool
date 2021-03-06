from django.contrib.auth.admin import UserAdmin
from django.contrib.gis import admin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Account


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account
    list_display = ('email', 'first_name', 'last_name', 'phone', 'state', 'is_driver', 'is_staff')
    list_filter = ('email', 'first_name', 'last_name', 'phone', 'state', 'is_driver', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone', 'street_address', 'city', 'state', 'zip_code', 'location', 'is_driver')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'street_address', 'city', 'state', 'zip_code', 
            'is_driver', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'phone', 'street_address', 'city', 'state', 'zip_code', 'is_driver')
    ordering = ('email',)


admin.site.register(Account, CustomUserAdmin)
