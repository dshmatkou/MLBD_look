import os
import json
from django.http import HttpResponse
from django.shortcuts import render
from web.endpoint.forms import UploadFileForm
from feature_extractor.model import Model


# Create your views here.

path_to_checkpoint = os.environ['WEIGHTS_DUMP']
model = Model(path_to_checkpoint)


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image_ar = form.files['file'].file.read()
            # redirect will work into dropone.js line 497
            features = model.extract_features(image_ar)
            print(str(features))
            static_link = '/star?static_url=pitt.jpg'

            return HttpResponse(json.dumps({'location': static_link}), content_type="application/json")
        else:
            raise Exception('Incorrect file')
    else:
        form = UploadFileForm()
    return render(request, 'endpoint/model_form_upload.html', {
        'form': form
    })


def star(request):
    return render(request, 'endpoint/show_star.html', context = {'static_url': 'endpoint/' + request.GET['static_url']})


def home(request):
    return render(request, 'endpoint/home.html')
