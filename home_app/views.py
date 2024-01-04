from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == 'POST':
        pass

    return render(request, 'home_app/index.html')
