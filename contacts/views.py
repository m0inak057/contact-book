from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Contact, UserLoginInfo
from django.contrib.auth.decorators import login_required # <-- Import login_required

# Create your views here.

@login_required  # <-- Secure this view
def contact_list(request):
    """Display all contacts for the logged-in user"""
    # Filter contacts by the logged-in user
    contacts = Contact.objects.filter(owner=request.user)
    query = request.GET.get('search', '')
    
    if query:
        contacts = contacts.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(address__icontains=query)
        )
    
    context = {
        'contacts': contacts,
        'query': query
    }
    return render(request, 'contacts/contact_list.html', context)

@login_required  # <-- Secure this view
def contact_create(request):
    """Create a new contact for the logged-in user"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()
        
        if not name:
            messages.error(request, 'Name is required.')
            return render(request, 'contacts/contact_form.html')
        
        # Check if contact already exists *for this user*
        if Contact.objects.filter(owner=request.user, name__iexact=name).exists():
            messages.error(request, f'Contact with name "{name}" already exists.')
            return render(request, 'contacts/contact_form.html')
        
        Contact.objects.create(
            owner=request.user,  # <-- Assign the owner
            name=name,
            phone=phone,
            email=email,
            address=address
        )
        messages.success(request, f'Contact "{name}" added successfully!')
        return redirect('contact_list')
    
    return render(request, 'contacts/contact_form.html')

@login_required  # <-- Secure this view
def contact_update(request, pk):
    """Update an existing contact, ensuring it belongs to the user"""
    # Get the contact *and* verify it belongs to the user
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        # ... (rest of your POST logic is good) ...
        
        if not name:
            messages.error(request, 'Name is required.')
            return render(request, 'contacts/contact_form.html', {'contact': contact})
        
        if Contact.objects.filter(owner=request.user, name__iexact=name).exclude(pk=pk).exists():
            messages.error(request, f'Another contact with name "{name}" already exists.')
            return render(request, 'contacts/contact_form.html', {'contact': contact})
        
        contact.name = name
        contact.phone = phone
        contact.email = email
        contact.address = address
        contact.save()
        
        messages.success(request, f'Contact "{name}" updated successfully!')
        return redirect('contact_list')
    
    return render(request, 'contacts/contact_form.html', {'contact': contact})

@login_required  # <-- Secure this view
def contact_delete(request, pk):
    """Delete a contact, ensuring it belongs to the user"""
    # Get the contact *and* verify it belongs to the user
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        name = contact.name
        contact.delete()
        messages.success(request, f'Contact "{name}" deleted successfully!')
        return redirect('contact_list')
    
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})


@login_required
def login_history(request):
    """Display login history for the current user"""
    login_records = UserLoginInfo.objects.filter(user=request.user)[:20]  # Last 20 logins
    
    context = {
        'login_records': login_records,
    }
    return render(request, 'contacts/login_history.html', context)