from django.urls import path
from wedding.views import index_view, story, photos, rsvp


urlpatterns = [
    path('', index_view, name='index'),
    path('index/', index_view, name='index'),
    path('story/', story, name='story'),
    path('photos/', photos, name='photos'),
    path('rsvp/', rsvp, name='rsvp'),
]