from django.shortcuts import render
from django.utils import timezone
from .models import New

# Create your views here.
def new_list(request):
    news = New.objects.filter(published_date=timezone.now()).order_by('published_date')
    return render(request, 'blogNews/new_list.html', {'news':news})