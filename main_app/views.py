from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Puppy, Clothes
from .forms import WalkingsForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def puppies_index(request):
    puppies = Puppy.objects.all()
    return render(request, 'puppies/index.html', {'puppies': puppies})

def puppies_detail(request, puppy_id):
    puppy = Puppy.objects.get(id=puppy_id)
    id_list = puppy.clothing.all().values_list('id')
    clothing_puppy_doesnt_have = Clothes.objects.exclude(id__in=id_list)
    walkings_form = WalkingsForm()
    return render(request, 'puppies/detail.html', {
        'puppy': puppy,
        'walkings_form': walkings_form,
        'clothing': clothing_puppy_doesnt_have
        })

def add_walkings(request, puppy_id):
    form = WalkingsForm(request.POST)
    if form.is_valid():
        new_walkings = form.save(commit=False)
        new_walkings.puppy_id= puppy_id
        new_walkings.save()
    return redirect('detail', puppy_id=puppy_id)

def assoc_clothes(request, puppy_id, clothes_id):
  Puppy.objects.get(id=puppy_id).clothing.add(clothes_id)
  return redirect('detail', puppy_id=puppy_id)

class PuppyCreate(CreateView):
    model = Puppy
    fields = ['name', 'breed', 'color', 'size', 'age']
    success_url = '/puppies/'

class PuppyUpdate(UpdateView):
    model = Puppy
    fields = ['breed', 'color', 'size', 'gender', 'age']

class PuppyDelete(DeleteView):
    model = Puppy
    success_url = '/puppies/'
    
    