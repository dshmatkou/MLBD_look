import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from web.endpoint.forms import UploadFileForm
from feature_extractor.model import Model
from web.endpoint.utils import load_index
from django.conf import settings


# Create your views here.

model = Model(settings.WEIGHTS_DUMP)
index = load_index()


class UploadView(View):

    def get(self, request):
        form = UploadFileForm()
        return render(request, 'endpoint/model_form_upload.html', {
            'form': form
        })

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image_ar = form.files['file'].file.read()
            # redirect will work into dropone.js line 497
            features = model.extract_features(image_ar)
            item = index.find_k_nearest(1, features)[0]

            return HttpResponse(
                json.dumps({'location': '/star?static_url=endpoint/' + item[0]}),
                content_type="application/json")
        else:
            return HttpResponseBadRequest('Incorrect file')


class StarView(View):

    def get(self, request):
        if 'static_url' in request.GET:
            return render(request, 'endpoint/show_star.html', context={'static_url': request.GET['static_url']})
        else:
            return render(request, 'endpoint/show_star.html')


class HomeView(View):

    def get(self, request):
        return render(request, 'endpoint/home.html')
