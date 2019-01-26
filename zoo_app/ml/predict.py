import numpy as np
import chainer
import chainer.links as L
from .GoogleNet import GoogleNet
from PIL import Image

def predict(model, path):
    x = Image.open(path)
    x = x.resize((224,224))
    x = np.array(x, dtype='f')
    x = x.transpose(2, 0, 1)
    x = x[np.newaxis, ...]
    y = model.predictor(x)[0]
    y = np.argmax(y.array)
    return y

def get_trained_model():
    model_path = 'zoo_app/ml/zoo_model.npz'
    trained_model =  L.Classifier(GoogleNet())
    chainer.serializers.load_npz(model_path, trained_model)
    return trained_model