import os
import json
from django.http import HttpResponse
from django.shortcuts import render
from web.endpoint.forms import UploadFileForm
from feature_extractor.model import Model
from web.endpoint.utils import load_index


# Create your views here.

path_to_checkpoint = os.environ['WEIGHTS_DUMP']
model = Model(path_to_checkpoint)
index = load_index()


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image_ar = form.files['file'].file.read()
            # redirect will work into dropone.js line 497
            features = model.extract_features(image_ar)
            item = index.find_k_nearest(1, features)[0]

            return HttpResponse(json.dumps({'location': '/star?static_url=endpoint/' + item[0]}), content_type="application/json")
        else:
            raise Exception('Incorrect file')
    else:
        form = UploadFileForm()
    return render(request, 'endpoint/model_form_upload.html', {
        'form': form
    })


def star(request):
    if 'static_url' in request.GET:
        return render(request, 'endpoint/show_star.html', context={'static_url': request.GET['static_url']})
    else:
        return render(request, 'endpoint/show_star.html')


def home(request):
    return render(request, 'endpoint/home.html')
