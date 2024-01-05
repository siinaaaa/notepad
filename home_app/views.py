from django.shortcuts import render, redirect
from .models import Note


# Create your views here.


def home(request):
    if request.method == 'POST':
        Note.objects.create(text=request.POST.get('text'))
        return redirect('/')

    return render(request, 'home_app/index.html')


def undo(request):
    notes = Note.objects.all()
    return render(request, 'home_app/indexes.html', {'notes': notes})


