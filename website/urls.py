"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import (
handler400, handler403, handler404, handler500
)
from django.conf.urls.static import static

admin.site.site_header = "Welcome to the Backend"
admin.site.site_title = "Shreyash"

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('backend.urls')),
    path('ul', include("urlshortner.urls")),
    path('todo_list/', include("todolist.urls")),
    path('dictionary/', include("dictionary.urls")),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler400 = "backend.views.bad_request"
handler403 = "backend.views.forbidden"
handler404 = "backend.views.page_not_found_view"
handler500 = "backend.views.server_error"

