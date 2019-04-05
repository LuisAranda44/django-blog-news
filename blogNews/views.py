from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import New
from .forms import NewForm


# Create your views here.
#Function Based Views
def new_list(request):
    news = New.objects.all().order_by('-published_date')
    return render(request, 'blogNews/new_list.html', {'news':news})

def new_detail(request,pk):
    new = get_object_or_404(New, pk=pk)
    return render(request, 'blogNews/new_detail.html', {'new': new})

def new_add(request):
    if request.method== "POST":
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save()
            return redirect('new_detail', pk=new.pk)
    else:
        form = NewForm()
    return render(request, 'blogNews/new_edit.html', {'form': form})

def new_edit(request,pk):
    new = get_object_or_404(New, pk=pk)
    if request.method == "POST":
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save()
            return redirect('new_detail', pk=new.pk)
    else:
        form = NewForm(instance=new)
    return render(request, 'blogNews/new_edit.html', {'form': form})

def new_delete(request, pk):
    new = get_object_or_404(New, pk=pk)
    if request.method == "POST":
        new.delete()
        return redirect('new_list',)
    return render(request, 'blogNews/new_delete.html', {'new': new})

#Class Based Views
class NewList(ListView):
    model = New
    template_name = 'blogNews/new_list_class.html'
    context_object_name = 'news'

class NewDetail(DetailView):
    #model = New
    template_name= 'blogNews/new_detail_class.html'
    queryset = New.objects.all()

class NewCreate(CreateView):
    model = New
    form_class = NewForm
    template_name= 'blogNews/new_edit_class.html'
    success_url = reverse_lazy('new_list_class')

class NewUpdate(UpdateView):
    model = New
    form_class = NewForm
    template_name = 'blogNews/new_edit_class.html'
    success_url = reverse_lazy('new_list_class')


class NewDelete(DeleteView):
    model = New
    template_name = 'blogNews/new_delete.html'
    success_url = reverse_lazy('new_list_class')
