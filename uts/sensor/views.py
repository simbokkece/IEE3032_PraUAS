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
    susutelur_protein = Sensor.objects.get(name="susutelur_protein")
    susutelur_omega = Sensor.objects.get(name="susutelur_omega")
    susutelur_salmonella = Sensor.objects.get(name="susutelur_salmonella")

    dagingmerah_muscle = Sensor.objects.get(name="dagingmerah_muscle")
    dagingmerah_darah = Sensor.objects.get(name="dagingmerah_darah")
    dagingmerah_metana = Sensor.objects.get(name="dagingmerah_metana")

    dagingputih_ecoli = Sensor.objects.get(name="dagingputih_ecoli")
    dagingputih_warna = Sensor.objects.get(name="dagingputih_warna")
    dagingputih_amonia = Sensor.objects.get(name="dagingputih_amonia")


    karbohidrat_volume = Sensor.objects.get(name="karbohidrat_volume")
    karbohidrat_kelembaban = Sensor.objects.get(name="karbohidrat_kelembaban")
    karbohidrat_oksigen = Sensor.objects.get(name="karbohidrat_oksigen")

    sayuran_urea = Sensor.objects.get(name="sayuran_urea")
    sayuran_cahaya = Sensor.objects.get(name="sayuran_cahaya")
    sayuran_temperatur = Sensor.objects.get(name="sayuran_temperatur")

    buah_pestisida = Sensor.objects.get(name="buah_pestisida")
    buah_ukuran = Sensor.objects.get(name="buah_ukuran")
    buah_berat = Sensor.objects.get(name="buah_berat")


    musim_angin = Sensor.objects.get(name="musim_angin")
    musim_listrik = Sensor.objects.get(name="musim_listrik")
    musim_barometer = Sensor.objects.get(name="musim_barometer")

    penjualan_barcode = Sensor.objects.get(name="penjualan_barcode")
    penjualan_cashflow = Sensor.objects.get(name="penjualan_cashflow")
    penjualan_infrared = Sensor.objects.get(name="penjualan_infrared")

    pengunjung_ultrasonic = Sensor.objects.get(name="pengunjung_ultrasonic")
    pengunjung_kamera = Sensor.objects.get(name="pengunjung_kamera")
    pengunjung_lidar = Sensor.objects.get(name="pengunjung_lidar")


    paru_alarm = 'media/green.jpg'
    lambung_alarm = 'media/green.jpg'
    jantung_alarm = 'media/green.jpg'


    context = {
        'paru_alarm' : str(paru_alarm),
        'lambung_alarm' : str(lambung_alarm),
        'jantung_alarm' : str(jantung_alarm),

        "susutelur_protein" : str(susutelur_protein.value),
        "susutelur_omega" : str(susutelur_omega.value),
        "susutelur_salmonella" : str(susutelur_salmonella.value),
        "dagingmerah_muscle" : str(dagingmerah_muscle.value),
        "dagingmerah_darah" : str(dagingmerah_darah.value),
        "dagingmerah_metana" : str(dagingmerah_metana.value),
        "dagingputih_ecoli" : str(dagingputih_ecoli.value),
        "dagingputih_warna" : str(dagingputih_warna.value),
        "dagingputih_amonia" : str(dagingputih_amonia.value),
        "karbohidrat_volume" : str(karbohidrat_volume.value),
        "karbohidrat_kelembaban" : str(karbohidrat_kelembaban.value),
        "karbohidrat_oksigen" : str(karbohidrat_oksigen.value),
        "sayuran_urea" : str(sayuran_urea.value),
        "sayuran_cahaya" : str(sayuran_cahaya.value),
        "sayuran_temperatur" : str(sayuran_temperatur.value),
        "buah_pestisida" : str(buah_pestisida.value),
        "buah_ukuran" : str(buah_ukuran.value),
        "buah_berat" : str(buah_berat.value),
        "musim_angin" : str(musim_angin.value),
        "musim_listrik" : str(musim_listrik.value),
        "musim_barometer" : str(musim_barometer.value),
        "penjualan_barcode" : str(penjualan_barcode.value),
        "penjualan_cashflow" : str(penjualan_cashflow.value),
        "penjualan_infrared" : str(penjualan_infrared.value),
        "pengunjung_ultrasonic" : str(pengunjung_ultrasonic.value),
        "pengunjung_kamera" : str(pengunjung_kamera.value),
        "pengunjung_lidar" : str(pengunjung_lidar.value)
    }

    return render(request, 'index.html', context)


def on_message_pro(client, userdata, msg):
    susutelur_protein = Sensor.objects.get(name="susutelur_protein")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(susutelur_protein, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new PROTEIN data ', msg.payload.decode('utf-8'))
    
def on_message_ome(client, userdata, msg):
    susutelur_omega = Sensor.objects.get(name="susutelur_omega")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(susutelur_omega, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new OMEGA data ', msg.payload.decode('utf-8'))
     
def on_message_sal(client, userdata, msg):
    susutelur_salmonella = Sensor.objects.get(name="susutelur_salmonella")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(susutelur_salmonella, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new CAPACITY data ', msg.payload.decode('utf-8'))


def on_message_mus(client, userdata, msg):
    dagingmerah_muscle = Sensor.objects.get(name="dagingmerah_muscle")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingmerah_muscle, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new ACIDITY data ', msg.payload.decode('utf-8'))

def on_message_dar(client, userdata, msg):
    dagingmerah_darah = Sensor.objects.get(name="dagingmerah_darah")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingmerah_darah, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new VOLUME data ', msg.payload.decode('utf-8'))

def on_message_met(client, userdata, msg):
    dagingmerah_metana = Sensor.objects.get(name="dagingmerah_metana")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingmerah_metana, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new TEMPERATURE data ', msg.payload.decode('utf-8'))


def on_message_eco(client, userdata, msg):
    dagingputih_ecoli = Sensor.objects.get(name="dagingputih_ecoli")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingputih_ecoli, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new BPM data ', msg.payload.decode('utf-8'))

def on_message_war(client, userdata, msg):
    dagingputih_warna = Sensor.objects.get(name="dagingputih_warna")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingputih_warna, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new SYSTOLE data ', msg.payload.decode('utf-8'))

def on_message_amo(client, userdata, msg):
    dagingputih_amonia = Sensor.objects.get(name="dagingputih_amonia")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingputih_amonia, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new DIASTOLE data ', msg.payload.decode('utf-8'))



def on_message_vol(client, userdata, msg):
    karbohidrat_volume = Sensor.objects.get(name="karbohidrat_volume")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(karbohidrat_volume, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new PROTEIN data ', msg.payload.decode('utf-8'))
    
def on_message_kel(client, userdata, msg):
    karbohidrat_kelembaban = Sensor.objects.get(name="karbohidrat_kelembaban")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(karbohidrat_kelembaban, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new OMEGA data ', msg.payload.decode('utf-8'))
     
def on_message_oxy(client, userdata, msg):
    karbohidrat_oksigen = Sensor.objects.get(name="karbohidrat_oksigen")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(karbohidrat_oksigen, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new CAPACITY data ', msg.payload.decode('utf-8'))


def on_message_ure(client, userdata, msg):
    sayuran_urea = Sensor.objects.get(name="sayuran_urea")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sayuran_urea, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new ACIDITY data ', msg.payload.decode('utf-8'))

def on_message_cah(client, userdata, msg):
    sayuran_cahaya = Sensor.objects.get(name="sayuran_cahaya")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sayuran_cahaya, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new VOLUME data ', msg.payload.decode('utf-8'))

def on_message_tem(client, userdata, msg):
    sayuran_temperatur = Sensor.objects.get(name="sayuran_temperatur")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sayuran_temperatur, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new TEMPERATURE data ', msg.payload.decode('utf-8'))


def on_message_pes(client, userdata, msg):
    buah_pestisida = Sensor.objects.get(name="buah_pestisida")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(buah_pestisida, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new BPM data ', msg.payload.decode('utf-8'))

def on_message_uku(client, userdata, msg):
    buah_ukuran = Sensor.objects.get(name="buah_ukuran")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(buah_ukuran, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new SYSTOLE data ', msg.payload.decode('utf-8'))

def on_message_ber(client, userdata, msg):
    buah_berat = Sensor.objects.get(name="buah_berat")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(buah_berat, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new DIASTOLE data ', msg.payload.decode('utf-8'))



def on_message_ang(client, userdata, msg):
    musim_angin = Sensor.objects.get(name="musim_angin")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(musim_angin, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new PROTEIN data ', msg.payload.decode('utf-8'))
    
def on_message_lis(client, userdata, msg):
    musim_listrik = Sensor.objects.get(name="musim_listrik")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(musim_listrik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new OMEGA data ', msg.payload.decode('utf-8'))
     
def on_message_bar(client, userdata, msg):
    musim_barometer = Sensor.objects.get(name="musim_barometer")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(musim_barometer, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new CAPACITY data ', msg.payload.decode('utf-8'))


def on_message_cod(client, userdata, msg):
    penjualan_barcode = Sensor.objects.get(name="penjualan_barcode")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(penjualan_barcode, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new ACIDITY data ', msg.payload.decode('utf-8'))

def on_message_cas(client, userdata, msg):
    penjualan_cashflow = Sensor.objects.get(name="penjualan_cashflow")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(penjualan_cashflow, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new VOLUME data ', msg.payload.decode('utf-8'))

def on_message_inf(client, userdata, msg):
    penjualan_infrared = Sensor.objects.get(name="penjualan_infrared")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(penjualan_infrared, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new TEMPERATURE data ', msg.payload.decode('utf-8'))


def on_message_ult(client, userdata, msg):
    pengunjung_ultrasonic = Sensor.objects.get(name="pengunjung_ultrasonic")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(pengunjung_ultrasonic, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new BPM data ', msg.payload.decode('utf-8'))

def on_message_kam(client, userdata, msg):
    pengunjung_kamera = Sensor.objects.get(name="pengunjung_kamera")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(pengunjung_kamera, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new SYSTOLE data ', msg.payload.decode('utf-8'))

def on_message_lid(client, userdata, msg):
    pengunjung_lidar = Sensor.objects.get(name="pengunjung_lidar")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(pengunjung_lidar, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    print('received a new DIASTOLE data ', msg.payload.decode('utf-8'))




client = mqtt.Client("sensor")

client.message_callback_add('susutelur/protein', on_message_pro)
client.message_callback_add('susutelur/omega', on_message_ome)
client.message_callback_add('susutelur/salmonella', on_message_sal)

client.message_callback_add('daingmerah/muscle', on_message_mus)
client.message_callback_add('daingmerah/darah', on_message_dar)
client.message_callback_add('daingmerah/metana', on_message_met)

client.message_callback_add('dagingputih/ecoli', on_message_eco)
client.message_callback_add('dagingputih/warna', on_message_war)
client.message_callback_add('dagingputih/amonia', on_message_amo)


client.message_callback_add('karbohidrat/volume', on_message_vol)
client.message_callback_add('karbohidrat/kelembaban', on_message_kel)
client.message_callback_add('karbohidratit/oksigen', on_message_oxy)

client.message_callback_add('sayuran/urea', on_message_ure)
client.message_callback_add('sayuran/cahaya', on_message_cah)
client.message_callback_add('sayuran/temperatur', on_message_tem)

client.message_callback_add('buah/pestisida', on_message_pes)
client.message_callback_add('buah/ukuran', on_message_uku)
client.message_callback_add('buah/berat', on_message_ber)


client.message_callback_add('musim/angin', on_message_ang)
client.message_callback_add('musim/listrik', on_message_lis)
client.message_callback_add('musim/barometer', on_message_bar)

client.message_callback_add('penjualan/barcode', on_message_cod)
client.message_callback_add('penjualan/cashflow', on_message_cas)
client.message_callback_add('penjualan/infrared', on_message_inf)

client.message_callback_add('pengunjung/ultrasonic', on_message_ult)
client.message_callback_add('pengunjung/kamera', on_message_kam)
client.message_callback_add('pengunjung/lidar', on_message_lid)

client.connect('localhost', 1883)
client.loop_start()
client.subscribe('#')