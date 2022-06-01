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


def projects_detail(request, pk):
    project = Projects.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'projects/project.html', context)



# class ExampleClassView(View):
#     """ Example Class Based View """
#     html='projects/index.html'
#     def get(self, request):
#         return render(request, self.html)
