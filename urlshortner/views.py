from django.shortcuts import render, redirect
import uuid
from .models import Url
from .forms import urls


# Create your views here.
def index(request):
    form = urls()
    if request.method == 'POST':
        form = urls(request.POST or None)
        if form.is_valid():
            link = form.links()
            uid = str(uuid.uuid4())[:5]
            new_url = Url(link=link, uuid=uid)
            new_url.save()
            context = {
                'form': form,
                'link': f"https://shreyash.pythonanywhere.com/{uid}"
            }
            return render(request, "Url_shortner.html", context)
    context = {
        'form': form,
    }
    return render(request, "Url_shortner.html", context)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)


