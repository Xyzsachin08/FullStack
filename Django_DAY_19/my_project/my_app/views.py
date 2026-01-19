from django.shortcuts import render
from .models import Contact
from .serialize import MyModelSerializer

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')

        Contact.objects.create(
            name=name,
            email=email,
            contact_number=contact_number
        )
    users = Contact.objects.all()
    serializer = MyModelSerializer(users, many=True) 

    return render(request, 'home.html',{'contacts': serializer.data})
