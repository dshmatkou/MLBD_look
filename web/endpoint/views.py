from django.http import HttpResponse
from django.shortcuts import render
from web.endpoint.forms import UploadFileForm


# Create your views here.


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image_ar = form.files['file'].file.read()
            print(image_ar)
            # redirect will work into dropone.js line 497
            return HttpResponse('')
        else:
            raise Exception('Incorrect file')
    else:
        form = UploadFileForm()
    return render(request, 'endpoint/model_form_upload.html', {
        'form': form
    })


def star(request):
    return render(request, 'endpoint/show_star.html')


def home(request):
    return render(request, 'endpoint/home.html')
