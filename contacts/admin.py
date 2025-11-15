from django.contrib import admin
from .models import Contact, UserLoginInfo

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('created_at',)


@admin.register(UserLoginInfo)
class UserLoginInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'login_time', 'ip_address', 'device_type', 'browser', 'os')
    search_fields = ('user__username', 'user__email', 'ip_address')
    list_filter = ('login_time', 'device_type', 'browser')
    readonly_fields = ('user', 'login_time', 'ip_address', 'user_agent', 'device_type', 'browser', 'os')
    
    def has_add_permission(self, request):
        # Prevent manual addition of login records
        return False
    
    def has_change_permission(self, request, obj=None):
        # Make records read-only
        return False
