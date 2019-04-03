from django.shortcuts import render, get_object_or_404
from .models import New
from .forms import NewForm
from django.shortcuts import redirect

# Create your views here.
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


