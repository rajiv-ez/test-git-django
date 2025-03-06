from django.http import HttpResponse

def index(request):
    return HttpResponse("Page d'accueil")

def contact(request):
    return HttpResponse("Page de contact")
