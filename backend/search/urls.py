from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('vidtube/', views.search_VidTube, name='search_VidTube'),
    path('library/<slug:library_type>', views.search_library, name='search_library'),
    path('tagged-playlists/<str:tag>', views.search_tagged_playlists, name='search_tagged_playlists'),
]
