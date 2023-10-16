from django.urls import path
from .views import home, projects, work
urlpatterns = [
    path('', home),
    path('work', work),
    path('project', projects),
]