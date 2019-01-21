from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import os
import numpy as np
import base64
from PIL import Image

import chainer
import chainer.links as L
from .GoogleNet import GoogleNet

from .models import Animal, AnimalInfo

model_path = 'zoo_app/zoo_model.npz'

trained_model =  L.Classifier(GoogleNet())
chainer.serializers.load_npz(model_path, trained_model)

def predict(model, path):
    x = Image.open(path)
    x = x.resize((224,224))
    x = np.array(x, dtype='f')
    x = x.transpose(2, 0, 1)
    x = x[np.newaxis, ...]
    y = model.predictor(x)[0]
    y = np.argmax(y.array)
    animal = Animal.objects.all().filter(id=y)[0]
    return animal

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file_obj = request.FILES['file']

        if form.is_valid():
            encoded = base64.b64encode(file_obj.read()).decode()
            mime = "image/jpg"
            mime = mime + ";" if mime else ";"
            input_image = "data:%sbase64,%s" % (mime, encoded)  
            print(input_image)
            animal = predict(trained_model, file_obj)
            animalinfo = AnimalInfo.objects.all().filter(animal=animal)
            return render(request, 'zoo_app/upload.html', {'form': form,  'image':input_image ,'animal': animal, 'animalinfo': animalinfo})
        else:
            return HttpResponse('invalid form')
    else:
        form = UploadFileForm()
    return render(request, 'zoo_app/upload.html', {'form': form})

