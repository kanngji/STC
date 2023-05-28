from django.shortcuts import render, redirect
from .models import Person
# Create your views here.

def index(request):
    comedian_list = Person.objects.order_by('name')
    context = {'comedian_list': comedian_list}
    return render(request, 'list/comedian_list.html', context)


# def person_create(request):
#     person = Person(name=request.POST.get('name'),gender=request.POST.get('gender'),nationality=request.POST.get('nationality'),representataive_work=request.POST.get('representataive_work'))
#     person.save()
#     return redirect('list:index')

def person_create(request):
    if request.method=='POST':
        person=Person()
        person.name = request.POST['name']
        person.gender = request.POST['gender']
        person.nationality = request.POST['nationality']
        person.representataive_work = request.POST['representataive_work']
        try:
            person.image=request.FILES['image']
        except: # 이미지가 없어도 그냥 지나가도록
            pass
        person.save()
        return redirect('list:index')
    