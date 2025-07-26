from django.shortcuts import render, redirect
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        Contact.objects.create(name=name, phone=phone, email=email)
        return redirect('contact_list')
    return render(request, 'contacts/contact_form.html')
