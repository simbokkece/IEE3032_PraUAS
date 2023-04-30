from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
import paho.mqtt.client as mqtt
import time

from .serializers import SensorSerializer
from .models import Sensor


# Create your views here.
def index(request):
    paru_oxy = Sensor.objects.get(name="paru_oxy")
    paru_tid = Sensor.objects.get(name="paru_tid")
    paru_cap = Sensor.objects.get(name="paru_cap")

    lambung_acid = Sensor.objects.get(name="lambung_acid")
    lambung_vol = Sensor.objects.get(name="lambung_vol")
    lambung_temp = Sensor.objects.get(name="lambung_temp")

    jantung_bpm = Sensor.objects.get(name="jantung_bpm")
    jantung_sys = Sensor.objects.get(name="jantung_sys")
    jantung_dia = Sensor.objects.get(name="jantung_dia")

    paru_alarm = 'media/green.jpg'
    lambung_alarm = 'media/green.jpg'
    jantung_alarm = 'media/green.jpg'

    if int(paru_oxy.value) <= 80 or 450 > int(paru_tid.value) > 750 or int(paru_cap.value) < 3500:
        paru_alarm = 'media/red.jpg'
    if float(lambung_acid.value) <= 3 or 30 > int(lambung_vol.value) > 90 or 45 < int(lambung_temp.value) < 35:
        lambung_alarm = 'media/red.jpg'
    if int(jantung_bpm.value) < 55 or 80 > int(jantung_sys.value) > 120 or 45 > int(jantung_dia.value) > 90:
        jantung_alarm = 'media/red.jpg'

    context = {
        'paru_oxy': str(paru_oxy.value),
        'paru_tid': str(paru_tid.value),
        'paru_cap': str(paru_cap.value),

        'lambung_acid': str(lambung_acid.value),
        'lambung_vol': str(lambung_vol.value),
        'lambung_temp': str(lambung_temp.value),

        'jantung_bpm': str(jantung_bpm.value),
        'jantung_sys': str(jantung_sys.value),
        'jantung_dia': str(jantung_dia.value),

        'paru_alarm' : str(paru_alarm),
        'lambung_alarm' : str(lambung_alarm),
        'jantung_alarm' : str(jantung_alarm)
    }

    return render(request, 'index.html', context)


def on_message_oxy(client, userdata, msg):
    paru_oxy = Sensor.objects.get(name="paru_oxy")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(paru_oxy, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new OXYGEN data ', msg.payload.decode('utf-8'))
    
def on_message_tid(client, userdata, msg):
    paru_tid = Sensor.objects.get(name="paru_tid")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(paru_tid, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new TIDAL data ', msg.payload.decode('utf-8'))
     
def on_message_cap(client, userdata, msg):
    paru_cap = Sensor.objects.get(name="paru_cap")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(paru_cap, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new CAPACITY data ', msg.payload.decode('utf-8'))



def on_message_acid(client, userdata, msg):
    lambung_acid = Sensor.objects.get(name="lambung_acid")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(lambung_acid, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new ACIDITY data ', msg.payload.decode('utf-8'))

def on_message_vol(client, userdata, msg):
    lambung_vol = Sensor.objects.get(name="lambung_vol")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(lambung_vol, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new VOLUME data ', msg.payload.decode('utf-8'))

def on_message_temp(client, userdata, msg):
    lambung_temp = Sensor.objects.get(name="lambung_temp")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(lambung_temp, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new TEMPERATURE data ', msg.payload.decode('utf-8'))



def on_message_bpm(client, userdata, msg):
    jantung_bpm = Sensor.objects.get(name="jantung_bpm")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(jantung_bpm, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new BPM data ', msg.payload.decode('utf-8'))

def on_message_sys(client, userdata, msg):
    jantung_sys = Sensor.objects.get(name="jantung_sys")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(jantung_sys, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new SYSTOLE data ', msg.payload.decode('utf-8'))

def on_message_dia(client, userdata, msg):
    jantung_dia = Sensor.objects.get(name="jantung_dia")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(jantung_dia, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new DIASTOLE data ', msg.payload.decode('utf-8'))



client = mqtt.Client("sensor")

client.message_callback_add('paru/oxygen', on_message_oxy)
client.message_callback_add('paru/tidal', on_message_tid)
client.message_callback_add('paru/capacity', on_message_cap)

client.message_callback_add('lambung/acid', on_message_acid)
client.message_callback_add('lambung/volume', on_message_vol)
client.message_callback_add('lambung/temp', on_message_temp)

client.message_callback_add('jantung/rate', on_message_bpm)
client.message_callback_add('jantung/systole', on_message_sys)
client.message_callback_add('jantung/diastole', on_message_dia)

client.connect('localhost', 1883)
client.loop_start()
client.subscribe('#')