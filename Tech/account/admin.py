from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    # SHOW ONLY FIELDS THAT EXIST IN YOUR USER MODEL
    list_display = ('id', 'email', 'name', 'role', 'is_staff', 'is_admin', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_admin', 'is_superuser', 'is_active')

    search_fields = ('email', 'name')
    ordering = ('id',)

    fieldsets = (
        ('Login Credentials', {'fields': ('email', 'password')}),
        
        ('Personal Information', {'fields': ('name', 'tc', 'role')}),

        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_admin',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),

        ('Important Dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )

    readonly_fields = ('created_at', 'updated_at')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'name',
                'tc',
                'role',
                'password1',
                'password2',
                'is_staff',
                'is_admin',
                'is_superuser',
            ),
        }),
    )
