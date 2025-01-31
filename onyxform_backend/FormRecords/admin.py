from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Display fields in the user list view
    list_display = ('last_name', 'email_address', 'is_active', 'is_staff')

    # Define the fields to display in the detailed form view (when editing a user)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name', 'last_name', 'title', 'age', 'citizenship', 'mobile_number', 
                'email_address', 'present_address', 'permanent_address', 'country_residence', 'valid_id', 'id_no', 
                'work_industry', 'role', 'income', 
                 'street_address'  # Newly added fields
            )
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define fields for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email_address', 'password1', 'password2'),
        }),
    )

# Register the CustomUser model with the customized admin
admin.site.register(CustomUser, CustomUserAdmin)
