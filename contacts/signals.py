from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import UserLoginInfo
from user_agents import parse


def get_client_ip(request):
    """Get the client's IP address from the request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """
    Signal handler that logs user information when they log in.
    This captures IP address, browser, OS, and device information.
    """
    # Get user agent string
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    
    # Parse user agent to extract browser, OS, and device info
    user_agent = parse(user_agent_string)
    
    # Determine device type
    if user_agent.is_mobile:
        device_type = 'Mobile'
    elif user_agent.is_tablet:
        device_type = 'Tablet'
    elif user_agent.is_pc:
        device_type = 'Desktop'
    else:
        device_type = 'Unknown'
    
    # Get IP address
    ip_address = get_client_ip(request)
    
    # Create login info record
    UserLoginInfo.objects.create(
        user=user,
        ip_address=ip_address,
        user_agent=user_agent_string,
        device_type=device_type,
        browser=f"{user_agent.browser.family} {user_agent.browser.version_string}",
        os=f"{user_agent.os.family} {user_agent.os.version_string}",
    )
    
    print(f"Login recorded for {user.username} from IP {ip_address} using {device_type}")
