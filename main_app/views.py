from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Guitarist
from .forms import VariationsForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitar_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', {'guitars': guitars})

def guitar_details(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    variations_form = VariationsForm()
    all_guitarists = Guitarist.objects.exclude(id__in = guitar.guitarists.all().values_list('id'))
    return render(request, 'guitars/details.html', {'guitar': guitar, 'variations_form': variations_form, 'all_guitarists': all_guitarists})
    
class GuitarCreate(CreateView):
  model = Guitar
  fields = '__all__'

class GuitarUpdate(UpdateView):
    model = Guitar
    fields = ['name', 'manufacturer', 'body_type', 'neck_joint', 'period_start', 'description']

class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars/'

def add_variations(request, guitar_id):
  form = VariationsForm(request.POST)
  if form.is_valid():
    new_variations = form.save(commit=False)
    new_variations.guitar_id = guitar_id
    new_variations.save()
  return redirect('detail', guitar_id=guitar_id)

def assoc_guitarist(request, guitar_id, guitarist_id):
  Guitar.objects.get(id=guitar_id).guitarists.add(guitarist_id)
  return redirect('detail', guitar_id=guitar_id)

def unassoc_guitarist(request, guitar_id, guitarist_id):
  Guitar.objects.get(id=guitar_id).guitarists.remove(guitarist_id)
  return redirect('detail', guitar_id=guitar_id)

class GuitaristCreate(CreateView):
  model = Guitarist
  fields = '__all__'

class GuitaristList(ListView):
  model = Guitarist

class GuitaristDetail(DetailView):
  model = Guitarist

class GuitaristUpdate(UpdateView):
  model = Guitarist
  fields = '__all__'

class GuitaristDelete(DeleteView):
  model = Guitarist
  success_url = '/guitarists/'

