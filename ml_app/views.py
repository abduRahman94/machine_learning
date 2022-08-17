from django.shortcuts import render
from model import Prediction


def index(request):
    return render(request, 'index.html')


def result(request):
    pclass = int(request.POST.get('pclass'))
    sexe = int(request.POST.get('sexe'))
    age = int(request.POST.get('age'))
    sibsp = int(request.POST.get('sibsp'))
    parch = int(request.POST.get('parch'))
    fare = int(request.POST.get('fare'))
    embC = int(request.POST.get('embC'))
    embQ = int(request.POST.get('embQ'))
    embS = int(request.POST.get('embS'))
    
    predictionModel = Prediction()
    resultat = predictionModel.getPrediction(pclass, sexe, age, sibsp, parch, fare, embC, embQ, embS)
    return render(request, 'resultat.html', {'resultat': resultat})