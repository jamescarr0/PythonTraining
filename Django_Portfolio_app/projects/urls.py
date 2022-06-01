from django.urls import path
from projects import views

urlpatterns = [
    path('', views.all_projects),
    path('<int:pk>', views.projects_detail),
]


# # Class Based View
# urlpatterns = [
#     path('', views.ExampleClassView.as_view())
# ]
