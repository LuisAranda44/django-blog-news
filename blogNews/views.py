from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import New

# Create your views here.
def new_list(request):
    news = New.objects.all().order_by('-published_date')
    return render(request, 'blogNews/new_list.html', {'news':news})

def new_detail(request,pk):
    new = get_object_or_404(New, pk=pk)
    return render(request, 'blogNews/new_detail.html', {'new': new})



