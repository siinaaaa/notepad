from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Modify


# Create your views here.


def home(request):
    counter = 0
    if request.method == 'POST':
        text = request.POST.get('text')
        note = Note.objects.filter(text=text)
        for item in note:
            counter += 1
        counter += 1
        note = Note.objects.create(text=request.POST.get('text'))
        modify = Modify.objects.first()
        modify.number = note.id
        modify.save()
        return render(request, 'home_app/indexes.html', {'number': counter})

    return render(request, 'home_app/indexes.html')


def undo(request):
    index = func_to_undo()
    note = get_object_or_404(Note, id=index)
    return render(request, 'home_app/indexes.html', {'notes': note})


def func_to_undo():
    modify = Modify.objects.first()
    index = modify.number - 1
    modify.number += -1
    modify.save()
    return index


def redo(request):
    index = func_to_redo()
    note = get_object_or_404(Note, id=index)
    return render(request, 'home_app/indexes.html', {'notes': note})


def func_to_redo():
    modify = Modify.objects.first()
    index = modify.number + 1
    modify.number += 1
    modify.save()
    return index
