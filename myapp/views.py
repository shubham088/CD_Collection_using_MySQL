from django.shortcuts import render
from .forms import AddCD
from .models import CD
# Create your views here.


def home(request):

    return render(request, 'myapp/home.html', {})



def add(request):

    if request.method == 'POST':

        form = AddCD(request.POST)

        if form.is_valid():
            form.save(commit = True)
    else:
        form = AddCD()

    return render(request, 'myapp/addcd.html', {'form' : form })



def see(request):

    data = CD.objects.all()
    print(data)
    return render(request, 'myapp/seecd.html', {'data' : data})
