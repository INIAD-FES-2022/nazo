from multiprocessing.connection import wait
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, Http404
from inya.models import Event, Search

# Create your views here.
# 脳筋コードだとは僕も思ってます
 
def index(request):
    try:
        event = Event.objects.get().event
        if (event == True):
            search = Search.objects.get(show=True)
            limit = search.limit
        else:
            search = Search.objects.get(wait=True)
            limit = "none"
        title = search.title
        text = search.text
    except:
        event = False
        title = "ERROR"
        text = "しばらく時間をおいてから再度お試しください"

    context = {
        "event": event,
        "title": title,
        "text": text,
        "limit": limit,
    }
    return render(request, 'inya/index.html', context)