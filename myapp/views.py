
from django.shortcuts import render
from .models import MyModel

def my_view(request):
    data = MyModel.objects.all()
    return render(request, 'myapp/index.html', {'data': data})

