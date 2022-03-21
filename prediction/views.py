from django.shortcuts import render
from .forms import PredictionForm, MultiplePredictionForm
from django.forms import formset_factory
from .models import Prediction

def home(request):
    return render(request, 'prediction/home.html')

def order(request):
    multiple_form = MultiplePredictionForm()
    if request.method == 'POST':
        created_prediction_pk = None
        filled_form = PredictionForm(request.POST)
        if filled_form.is_valid():
            created_prediction = filled_form.save()
            created_prediction_pk = created_prediction.id
            note = 'Thanks for ordering! Your %s %s and %s prediction is on its way!' %(filled_form.cleaned_data['size'], filled_form.cleaned_data['ticker'], filled_form.cleaned_data['days'],)
            filled_form = PredictionForm()
        else:
            note = 'Order was not created, please try again'
        new_form = PredictionForm()
        return render(request, 'prediction/order.html', {'multiple_form':multiple_form, 'PredictionForm':filled_form, 'note':note, 'created_prediction_pk':created_prediction_pk})
    else:
        form = PredictionForm()
        return render(request, 'prediction/order.html', {'multiple_form':multiple_form, 'PredictionForm':form})

def edit_order(request,pk):
    prediction = prediction.objects.get(pk=pk)
    form = PredictionForm(instance=prediction)
    if request.method == 'POST':
        filled_form = PredictionForm(request.POST, instance=prediction)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Your order has been processed.'
            return render(request, 'prediction/edit_order.html', {'PredictionForm':form, 'prediction':prediction, 'note':note})
    return render(request, 'prediction/edit_order.html', {'PredictionForm':form, 'prediction':prediction})


def predictions(request):
    number_of_predictions = 2
    filled_multiple_prediction_form = MultiplePredictionForm(request.GET)
    if filled_multiple_prediction_form.is_valid():
        number_of_predictions = filled_multiple_prediction_form.cleaned_data['number']
    PredictionFormSet = formset_factory(PredictionForm, extra=number_of_predictions)
    formset = PredictionFormSet()
    if request.method == "POST":
        filled_formset = PredictionFormSet(request.POST)
        if(filled_formset.is_valid()):
            for form in filled_formset:
                print(form.cleaned_data['ticker'])
            note = 'predictions have been ordered!'
        else:
            note = 'Order was not created, please try again'


        return render(request, 'prediction/prediction.html', {'note':note, 'formset':formset})
    else:
        return render(request, 'prediction/prediction.html', {'formset':formset})
