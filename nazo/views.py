from pickle import NEXT_BUFFER
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, Http404
from nazo.models import Nazo, Answer

# Create your views here.

def index(request):
    return render(request, 'nazo/index.html')

def tutorial(request):
    try:
        tutorial = Nazo.objects.get(tutorial=True)
        uuid = tutorial.uuid
    except Nazo.DoesNotExist:
        raise Http404("この謎ないね")
    context = {
        "uuid": uuid,
    }
    return render(request, 'nazo/tutorial.html', context)

def nazo(request, nazo_id):
    try:
        nazo = Nazo.objects.get(uuid=nazo_id)
        title = nazo.title
        difficulty = nazo.difficulty
        minihint = nazo.minihint
        input = nazo.input
        img = nazo.img
        nazo_uuid = nazo.uuid
        answer = Answer.objects.get(nazo_number=nazo_uuid)
        answer_uuid = answer.uuid
        last_nazo = nazo.last_nazo
        border_color = answer.border_color
    except Nazo.DoesNotExist:
        raise Http404("この謎ないね")
    context = {
        "title": title,
        "difficulty": difficulty,
        "minihint": minihint,
        "input": input,
        "img": img,
        "answer_uuid": answer_uuid,
        "last_nazo": last_nazo,
        "border_color": border_color,
    }    
    return render(request, 'nazo/nazo.html', context)

def answer(request, answer_id):
    try:
        answer = Answer.objects.get(uuid=answer_id)
        input_answer = answer.input_answer
        next_place = answer.next_place
        img = answer.img
        border_color = answer.border_color
        keyword = answer.keyword

        nazo_place = answer.nazo_number
        nazo_id = nazo_place.uuid
        nazo = Nazo.objects.get(uuid=nazo_id)
        title = nazo.title
        hint = nazo.hint
        big_hint = nazo.big_hint
        tutorial = nazo.tutorial
        last_nazo_check = nazo.last_nazo
        last_nazo_data = Nazo.objects.get(last_nazo=True)
        last_uuid_data = last_nazo_data.uuid
        try:
            player_answer = request.POST["player_answer"]
        except:
            player_answer = ""
    except Nazo.DoesNotExist:
        raise Http404("この謎ないね")

    if (player_answer == input_answer):
        result = True
    else:
        result = False

    context = {
        "title": title,
        "next_place": next_place,
        "img": img,
        "border_color": border_color,
        "keyword": keyword,
        "hint": hint,
        "big_hint": big_hint,
        "tutorial": tutorial,
        "result": result,
        "last_nazo_check": last_nazo_check,
        "last_uuid_data": last_uuid_data,
    }    
    return render(request, 'nazo/answer.html', context)