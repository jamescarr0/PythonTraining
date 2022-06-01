from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from projects.models import Projects

# Create your views here.
def all_projects(request):
    # Query the db to return all project objects.
    projects = Projects.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/all_projects.html', context=context)

def projects_list(request):
    return render(request, 'projects/index.html')

class ExampleClassView(View):
    """ Example Class Based View """
    html='projects/index.html'
    def get(self, request):
        return render(request, self.html)
