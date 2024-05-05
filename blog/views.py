from django.shortcuts import render
from django.views import View
# Create your views here.


# def IndexView(request):
#     return render(request, 'index.html')


class MyView(View):
    def get(self, request):
        return render(request, 'index-2.html')


class SayHello(View):
    def get(self, request):
        return render(request, 'hello.html', {'name': 'Rafi'})
