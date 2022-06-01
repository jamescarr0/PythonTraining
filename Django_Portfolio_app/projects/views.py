from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def projects_list(request):
    return render(request, 'projects/index.html')

class ExampleClassView(View):
    html=None
    def get(self, request):
        return render(request, self.html)
