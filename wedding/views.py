from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, "wedding/index.html")

def story(request):
    return render(request, "wedding/story.html")

def photos(request):
    return render(request, "wedding/photos.html")

def rsvp(request):
    return render(request, "wedding/rsvp.html")