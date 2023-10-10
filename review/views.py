from urllib.parse import urlparse

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET


# Create your views here.
@require_GET
def index(request):
    return HttpResponse("This is the Review Index")


def redirect(request):

    url = request.GET.get("url", '/')
    return HttpResponseRedirect(url)
