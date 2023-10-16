from django.urls import path
from . import views

urlpatterns = [
    path('url_shortner/', views.index, name="shortner"),
    path('<str:pk>', views.go, name="go")
]