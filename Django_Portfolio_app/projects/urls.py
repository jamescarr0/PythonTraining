from django.urls import path
from projects import views


urlpatterns = [
    path('', views.ExampleClassView.as_view(html='projects/index.html'))
]