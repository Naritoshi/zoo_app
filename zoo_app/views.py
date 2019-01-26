from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .util import util
from .ml import predict
from .models import Animal, AnimalInfo

trained_model =  predict.get_trained_model()

#@login_required
def main(request):
    if request.method == 'POST' and request.FILES['file']:
        if util.get_extntion(request.FILES['file'].name).upper() == '.JPG':
            #表示用の画像形式にする
            input_image = util.create_image_data(request.FILES['file'].read())
            #予測する
            y = predict.predict(trained_model, request.FILES['file'])
            #ラベルにあった動物を取得する
            animal = Animal.objects.all().filter(id=y)[0]
            #動物にあった文言を取得する
            animalinfo = AnimalInfo.objects.all().filter(animal=animal)
            return render(request, 'zoo_app/main.html', {'image':input_image ,'animal': animal, 'animalinfo': animalinfo})
        else:
            return render(request, 'zoo_app/main.html', {'error_msg': '拡張子は、JPGのみ対応しています。'})
    else:
        return render(request, 'zoo_app/main.html')
