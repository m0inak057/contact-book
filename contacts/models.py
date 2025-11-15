from django.db import models
from django.contrib.auth.models import User # <-- Import the User model


class UserLoginInfo(models.Model):
    """Track user login information"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_info')
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)  # Browser info
    device_type = models.CharField(max_length=50, blank=True)  # Mobile, Desktop, etc.
    browser = models.CharField(max_length=100, blank=True)
    os = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)  # Optional: can add geolocation
    
    class Meta:
        ordering = ['-login_time']
        verbose_name = 'User Login Info'
        verbose_name_plural = 'User Login Info'
    
    def __str__(self):
        return f"{self.user.username} - {self.login_time}"


class Contact(models.Model):
    # Add this field to link a Contact to a User
    # We use null=True, blank=True so existing contacts don't break the database
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    name = models.CharField(max_length=100) # Removed unique=True
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        # Add this to allow multiple users to have a contact with the same name
        unique_together = [['owner', 'name']] 
    
    def __str__(self):
        return self.name