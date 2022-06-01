from django.urls import path
from projects import views

urlpatterns = [
    path('', views.all_projects),
    path('test', views.projects_list),
]


# # Class Based View
# urlpatterns = [
#     path('', views.ExampleClassView.as_view())
# ]
