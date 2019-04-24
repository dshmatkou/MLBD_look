from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from web.endpoint.forms import UploadFileForm


# Create your views here.


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image_ar = form.files['file'].file.read()
            print(image_ar)
            return HttpResponseRedirect(reverse('star'))
    else:
        form = UploadFileForm()
    return render(request, 'endpoint/model_form_upload.html', {
        'form': form
    })


def star(request):
    return render(request, 'endpoint/show_star.html')


def home(request):
    return render(request, 'endpoint/home.html')
