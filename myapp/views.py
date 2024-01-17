# myapp/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            person = Person.objects.create(name=name)

            # passes the private key of the created object, that is the name
            return redirect('welcome', pk=person.pk)
        else:
            return HttpResponse("Invalid form submission. Name cannot be empty.")
    else:
        return render(request, 'myapp/index.html')

def welcome(request, pk):
    person = Person.objects.get(pk=pk)
    return render(request, 'myapp/welcome.html', {'person': person})