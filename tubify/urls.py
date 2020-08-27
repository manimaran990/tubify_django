from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search_tube'),
    path('getmp3/<str:id>', views.get_music, name='get_music')
]