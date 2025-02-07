from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Ensure 'email_address' and 'signature' are displayed
    list_display = ('email_address', 'last_name', 'is_active', 'is_staff', 'signature')

    fieldsets = (
        (None, {'fields': ('email_address', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name', 'last_name', 'title', 'age', 'date_of_birth', 'place_of_birth', 'gender', 'nationality', 'mobile_number',
                'same_address', 'street_address', 'city_residence', 'state_residence',
                'permanent_street_address', 'permanent_city', 'permanent_state', 'valid_id', 'id_no', 'valid_until',
                'id_front', 'id_back', 'signature',  # ✅ Added signature
                'work_industry', 'role', 'income', 'marketing_consent', 'privacy_consent',
            ),
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email_address', 'password1', 'password2'),
        }),
    )

# Register the CustomUser model with the customized admin
admin.site.register(CustomUser, CustomUserAdmin)
