from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact

# CREATE + READ
def home(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            contact_number=request.POST['contact_number']
        )
        return redirect('/')

    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})


# UPDATE
def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.contact_number = request.POST['contact_number']
        contact.save()
        return redirect('/')

    return render(request, 'edit.html', {'contact': contact})


# DELETE
def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('/')
