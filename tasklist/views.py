from .models import Task

from django.http import HttpResponse


def index(request):
    collection = Task.objects.all()
    return HttpResponse(collection)
