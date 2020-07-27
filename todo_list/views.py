from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
  
  if request.method == 'POST':
    form = ListForm(request.POST or None)
    if form.is_valid():
      form.save()
      messages.success(request, ('Item has been added!'))
      return redirect('home')
  else:
    data = {}
    data['items'] = List.objects.all()
    return render(request, 'home.html', data)


def about(request): 
  return render(request, 'about.html')

def delete(request, list_id):
  item = List.objects.get(pk=list_id)
  item.delete()
  messages.warning(request, ('Item has been deleted!'))
  return redirect('home')

def cross_off(request, list_id):
  item = List.objects.get(pk=list_id)
  item.completed = True
  item.save()
  return redirect('home')

def uncross(request, list_id):
  item = List.objects.get(pk=list_id)
  item.completed = False
  item.save()
  return redirect('home')

def edit(request, list_id):
  item = List.objects.get(pk=list_id)

  if request.method == 'POST':
    form = ListForm(request.POST or None, instance=item)
    if form.is_valid():
      form.save()
      messages.success(request, ('Item has been edited!'))
      return redirect('home')
  else:
    data = {}
    data['items'] = List.objects.get(pk=list_id)
    return render(request, 'edit.html', data)