from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def work(request):
    return render(request, 'work.html')


def projects(request):
    return render(request, 'project.html')



def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def server_error(request, exception=None):
    return render(request, '500.html', status=500)


def bad_request(request, exception=None):
    return render(request, '400.html', status=400)


def forbidden(request, exception=None):
    return render(request, '403.html', status=403)
