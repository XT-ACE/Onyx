from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.urls import reverse
from .models import CustomMember

class CustomMemberAdmin(UserAdmin):
    model = CustomMember

    list_display = ('id_link', 'email_address', 'last_name', 'signature')

    def id_link(self, obj):
        profile_url = f"http://192.168.1.11:5173/profile/{obj.id}"
        admin_edit_url = reverse('admin:FormRecords_custommember_change', args=[obj.id])
        return format_html(
            '<a href="{}" target="_blank">🔗 Profile</a> | <a href="{}">✏️ Edit</a>',
            profile_url, admin_edit_url
        )

    id_link.short_description = "Actions"

    base_fieldsets = (
        ('Member info', {
            'fields': (
                'first_name', 'last_name',  'email_address', 'title', 'age', 'date_of_birth', 'place_of_birth', 'gender', 'nationality', 'mobile_number',
                'same_address', 'street_address', 'city_residence', 'state_residence',
                'permanent_street_address', 'permanent_city', 'permanent_state', 'valid_id', 'id_no', 'valid_until',
                'id_front', 'id_back', 'signature',
                'work_industry', 'role', 'income', 'marketing_consent', 'privacy_consent','agreeToPrivacy','isOver21',
            ),
        }),
    )

    permissions_fieldset = ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')})

    def get_fieldsets(self, request, obj=None):
        """Only show the 'Permissions' section to superusers."""
        fieldsets = list(self.base_fieldsets)
        if request.user.is_superuser:
            fieldsets.insert(2, self.permissions_fieldset)  # Insert Permissions section
        return fieldsets

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email_address', 'password1', 'password2'),
        }),
    )

# Register the CustomUser model with the customized admin
admin.site.register(CustomMember, CustomMemberAdmin)
admin.site.site_header = "Onyx Casino"
admin.site.site_title = "Onyx Casino Admin Portal"
admin.site.index_title = "Welcome to Onyx Casino Administration"
