from django.http import HttpResponse
from django.shortcuts import render
from web.endpoint.forms import UploadFileForm
from feature_extractor import model as model_lib


# Create your views here.

path_to_checkpoint = './checkpoints/resnet_v1_101_2016_08_28/resnet_v1_101.ckpt'
model = model_lib.Model(path_to_checkpoint)

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image_ar = form.files['file'].file.read()
            print(image_ar)
            # redirect will work into dropone.js line 497

            features = model.extract_features()

            return HttpResponse(str(features))
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
