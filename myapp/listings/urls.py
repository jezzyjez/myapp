from django.urls import path, re_path
from .import views


urlpatterns = [ 
        re_path(r'^movie_list$', views.movie_list, name='movie_list'),
        re_path(r'^song_list$', views.song_list, name='song_list'),
        re_path(r'^book_list$', views.book_list, name='book_list'),
        re_path(r'^add/(?P<list_type>movie|song|book)/', views.add_data, name='add_data'),
        re_path(r'^remove/(?P<list_type>movie|song|book)/(?P<pk>\d+)', views.remove_list, name='remove'),
        re_path(r'^edit/(?P<list_type>movie|song|book)/(?P<pk>\d+)', views.edit_data, name='edit_data'),
        ]
