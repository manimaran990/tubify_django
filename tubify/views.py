from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from background_task import background
from django.core import serializers
from django.contrib import messages

from tubify.utils.tube_search import Tube_search
from tubify.utils.drop_to_box import Drop_to_Box
from tubify.utils.tube_dl import Tubedl

from .models import Tubify

#global list
info_list = None

# Create your views here.


def home(request):
    ts = Tube_search("jojo all ending", 10)
    global info_list
    info_list = ts.get_info()
    context = {
        "info_list": info_list
    }
    return render(request, 'tubify/home.html', context)


def search(request):
    global search_qry
    search_qry = request.POST.get('search_query', False)
    ts = Tube_search(search_qry, 20)
    global info_list
    info_list = ts.get_info()
    context = {
        "info_list": info_list
    }
    return render(request, 'tubify/home.html', context)

@background(queue='my-queue')
def yt_to_dbx(id):
    d_url = f'https://www.youtube.com/watch?v={id}'

    # tube dl object
    td = Tubedl()

    # dropbox path to save the files
    dbx_path = '/'
    dbx = Drop_to_Box('config.cfg')

    td.get_audio(d_url, dbx, dbx_path)


def get_music(request, id):
    yt_to_dbx(id)
    
    for item in info_list:
        if item.get('v_url_suffix', None) == id:
            id = item.get('v_id', None)
            title = item.get('v_title', None)
            views = item.get('v_views', None)
            thumb = item.get('v_thumb', None)
            url_suffix = item.get('v_url_suffix', None)
            t = Tubify(v_id=id, v_title=title, v_views = views, v_thumb=thumb, v_url_suffix=url_suffix)
            t.save()

    context = {
        "info_list": info_list
    }
    messages.info(request, "request added to queue!!!")
    return render(request, 'tubify/home.html', context)
   
