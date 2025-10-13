from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Contact

# Create your views here.

def contact_list(request):
    """Display all contacts"""
    contacts = Contact.objects.all()
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

def contact_create(request):
    """Create a new contact"""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()
        
        # Validation
        if not name:
            messages.error(request, 'Name is required.')
            return render(request, 'contacts/contact_form.html')
        
        # Check if contact already exists
        if Contact.objects.filter(name__iexact=name).exists():
            messages.error(request, f'Contact with name "{name}" already exists.')
            return render(request, 'contacts/contact_form.html')
        
        # Create contact
        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            address=address
        )
        messages.success(request, f'Contact "{name}" added successfully!')
        return redirect('contact_list')
    
    return render(request, 'contacts/contact_form.html')

def contact_update(request, pk):
    """Update an existing contact"""
    contact = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        address = request.POST.get('address', '').strip()
        
        # Validation
        if not name:
            messages.error(request, 'Name is required.')
            return render(request, 'contacts/contact_form.html', {'contact': contact})
        
        # Check if name conflicts with another contact
        if Contact.objects.filter(name__iexact=name).exclude(pk=pk).exists():
            messages.error(request, f'Another contact with name "{name}" already exists.')
            return render(request, 'contacts/contact_form.html', {'contact': contact})
        
        # Update contact
        contact.name = name
        contact.phone = phone
        contact.email = email
        contact.address = address
        contact.save()
        
        messages.success(request, f'Contact "{name}" updated successfully!')
        return redirect('contact_list')
    
    return render(request, 'contacts/contact_form.html', {'contact': contact})

def contact_delete(request, pk):
    """Delete a contact"""
    contact = get_object_or_404(Contact, pk=pk)
    
    if request.method == 'POST':
        name = contact.name
        contact.delete()
        messages.success(request, f'Contact "{name}" deleted successfully!')
        return redirect('contact_list')
    
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})
