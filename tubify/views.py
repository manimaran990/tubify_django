from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from background_task import background
from django.core import serializers

from tubify.utils.tube_search import Tube_search
from tubify.utils.drop_to_box import Drop_to_Box
from tubify.utils.tube_dl import Tubedl

#global list
search_qry = []

# Create your views here.


def home(request):
    ts = Tube_search("jojo all ending", 10)
    context = {
        "info_list": ts.get_info()
    }
    return render(request, 'tubify/home.html', context)


def search(request):
    global search_qry
    search_qry = request.POST.get('search_query', False)
    ts = Tube_search(search_qry, 20)
    context = {
        "info_list": ts.get_info()
    }
    return render(request, 'tubify/home.html', context)



def get_music(request, id):
    d_url = f'https://www.youtube.com/watch?v={id}'

    # tube dl object
    td = Tubedl()

    # dropbox path to save the files
    dbx_path = '/'
    dbx = Drop_to_Box('config.cfg')

    td.get_audio(d_url, dbx, dbx_path)

    response_data = serializers.serialize(
        'json', {"message": "successfully triggered get_music"})

    return HttpResponse(response_data)

    # return HttpResponse(json.dumps())

    # ts = Tube_search(search_qry, 20)
    # context = {
    #     "info_list": ts.get_info()
    # }

    # return render(request, 'tubify/home.html', context)
