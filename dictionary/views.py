from django.shortcuts import render
from PyDictionary import PyDictionary


# Create your views here.
def index(request):
    return render(request, 'dictionary.html')


def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    grammer = ['Noun', 'Adjective', 'Adverb', 'Verb']
    a = " "
    for b in grammer:
        try:
            k = meaning[b][0]
            a = a + k
            meaning = a
        except:
            continue
    context = {
        'meaning': meaning,
        'word': search,
    }
    return render(request, 'word.html', context)
