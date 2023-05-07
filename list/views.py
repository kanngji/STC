from django.shortcuts import render, redirect
from .models import Person
# Create your views here.

def index(request):
    comedian_list = Person.objects.order_by('name')
    context = {'comedian_list': comedian_list}
    return render(request, 'list/comedian_list.html', context)


def person_create(request):
    person = Person(name=request.POST.get('name'),gender=request.POST.get('gender'),nationality=request.POST.get('nationality'),representataive_work=request.POST.get('representataive_work'))
    person.save()
    return redirect('list:index')