from datetime import date

from variables.logic.variables_logic import get_variable
from ..models import Measurement

def get_measurements():
    measurements =  Measurement.objects.all()
    return measurements

def get_measurement(me_pk):
    measurement = Measurement.objects.get(pk=me_pk)
    return measurement

def create_measurement(me):
    measurement = Measurement(variable=get_variable(me["variable"]), 
                                value= me["value"],
                                unit= me["unit"],
                                place= me["place"],
                                dateTime= me["dateTime"])
    measurement.save()
    return measurement

def update_measurement(me_pk, new_me):
    measurement = get_measurement(me_pk)
    measurement.variable = get_variable(new_me["variable"])
    measurement.value = new_me["value"]
    measurement.unit = new_me["unit"]
    measurement.place = new_me["place"]
    measurement.dateTime = new_me["dateTime"]
    measurement.save()
    return measurement

def delete_measurement(me_pk):
    measurement = get_measurement(me_pk)
    measurement.delete()
    return measurement