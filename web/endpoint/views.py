from django.http import HttpResponse
from pyindex import pysum

# Create your views here.


def endpoint(request):
    x = int(request.GET.get('x', '1'))
    y = int(request.GET.get('y', '2'))
    return HttpResponse('Result is: ' + str(pysum(x, y)))
