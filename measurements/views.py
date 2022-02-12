from re import M
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render
from django.core import serializers
from .logic import measurements_logic as ml
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = ml.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            measurements_dto = ml.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, 'application/json')
    elif request.method == 'POST':
        measurement_dto = ml.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json',[measurement_dto,])
        return HttpResponse(measurement_dto, 'application/json')
    elif request.method == 'DELETE':
        return HttpResponseBadRequest()
    else:
        return HttpResponseNotFound()
@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = ml.get_measurement(pk)
        measurement = serializers.serialize('json',[measurement_dto,])
        return HttpResponse(measurement,'application/json')
    elif request.method == 'PUT' or request.method == 'PATCH':
        measurement_dto = ml.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json',[measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    elif request.method == 'DELETE':
        measurement_dto = ml.delete_measurement(pk)
        measurement = serializers.serialize('json',[measurement_dto,])
        return HttpResponse(measurement, 'application/json')