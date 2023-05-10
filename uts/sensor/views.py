from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
import paho.mqtt.client as mqtt
import time

from ml_model import machinelearning

from .serializers import SensorSerializer
from .models import Sensor


# Create your views here.
def index(request):
    model1 = machinelearning.ml_susutelur
    model2 = machinelearning.ml_dagingmerah
    model3 = machinelearning.ml_dagingputih
    model4 = machinelearning.ml_karbohidrat
    model5 = machinelearning.ml_sayuran
    model6 = machinelearning.ml_buah
    model7 = machinelearning.ml_musim 
    model8 = machinelearning.ml_penjualan 
    model9 = machinelearning.ml_pengunjung 
    model10 = machinelearning.ml_perawatan 
    model11 = machinelearning.ml_panen
    model12 = machinelearning.ml_promosi
    model13 = machinelearning.ml_keuntungan
    
    
    susutelur_protein = Sensor.objects.get(name="susutelur_protein")
    susutelur_omega = Sensor.objects.get(name="susutelur_omega")
    susutelur_salmonella = Sensor.objects.get(name="susutelur_salmonella")

    predict1 = model1.predict([float(susutelur_protein.value), float(susutelur_omega.value), float(susutelur_salmonella.value)])


    dagingmerah_muscle = Sensor.objects.get(name="dagingmerah_muscle")
    dagingmerah_darah = Sensor.objects.get(name="dagingmerah_darah")
    dagingmerah_metana = Sensor.objects.get(name="dagingmerah_metana")

    predict2 = model2.predict([float(dagingmerah_muscle.value), float(dagingmerah_darah.value), float(dagingmerah_metana.value)])


    dagingputih_ecoli = Sensor.objects.get(name="dagingputih_ecoli")
    dagingputih_warna = Sensor.objects.get(name="dagingputih_warna")
    dagingputih_amonia = Sensor.objects.get(name="dagingputih_amonia")

    predict3 = model3.predict([float(dagingputih_ecoli.value), float(dagingputih_warna.value), float(dagingputih_amonia.value)])


    karbohidrat_volume = Sensor.objects.get(name="karbohidrat_volume")
    karbohidrat_kelembaban = Sensor.objects.get(name="karbohidrat_kelembaban")
    karbohidrat_oksigen = Sensor.objects.get(name="karbohidrat_oksigen")

    predict4 = model4.predict([float(karbohidrat_volume.value), float(karbohidrat_kelembaban.value), float(karbohidrat_oksigen.value)])


    sayuran_urea = Sensor.objects.get(name="sayuran_urea")
    sayuran_cahaya = Sensor.objects.get(name="sayuran_cahaya")
    sayuran_temperatur = Sensor.objects.get(name="sayuran_temperatur")

    predict5 = model5.predict([float(sayuran_urea.value), float(sayuran_cahaya.value), float(sayuran_temperatur.value)])


    buah_pestisida = Sensor.objects.get(name="buah_pestisida")
    buah_ukuran = Sensor.objects.get(name="buah_ukuran")
    buah_berat = Sensor.objects.get(name="buah_berat")

    predict6 = model6.predict([float(buah_pestisida.value), float(buah_ukuran.value), float(buah_berat.value)])


    musim_angin = Sensor.objects.get(name="musim_angin")
    musim_listrik = Sensor.objects.get(name="musim_listrik")
    musim_barometer = Sensor.objects.get(name="musim_barometer")

    predict7 = model7.predict([float(musim_angin.value), float(musim_listrik.value), float(musim_barometer.value)])


    penjualan_barcode = Sensor.objects.get(name="penjualan_barcode")
    penjualan_cashflow = Sensor.objects.get(name="penjualan_cashflow")
    penjualan_infrared = Sensor.objects.get(name="penjualan_infrared")

    predict8 = model8.predict([float(penjualan_barcode.value), float(penjualan_cashflow.value), float(penjualan_infrared.value)])


    pengunjung_ultrasonic = Sensor.objects.get(name="pengunjung_ultrasonic")
    pengunjung_kamera = Sensor.objects.get(name="pengunjung_kamera")
    pengunjung_lidar = Sensor.objects.get(name="pengunjung_lidar")

    predict9 = model9.predict([float(pengunjung_ultrasonic.value), float(pengunjung_kamera.value), float(pengunjung_lidar.value)])


    predict10 = model10.predict([float(predict1[0][0]), float(predict2[0][0]), float(predict3[0][0])])
    predict11 = model11.predict([float(predict4[0][0]), float(predict5[0][0]), float(predict6[0][0])])
    predict12 = model12.predict([float(predict7[0][0]), float(predict8[0][0]), float(predict9[0][0])])
    predict13 = model13.predict([float(predict10[0][0]), float(predict11[0][0]), float(predict12[0][0])])

    print(predict10)

    alarm1 = 'media/green.jpg'
    alarm2 = 'media/green.jpg'
    alarm3 = 'media/green.jpg'
    alarm4 = 'media/green.jpg'
    alarm5 = 'media/green.jpg'
    alarm6 = 'media/green.jpg'
    alarm7 = 'media/green.jpg'
    alarm8 = 'media/green.jpg'
    alarm9 = 'media/green.jpg'
    alarm10 = 'media/green.jpg'
    alarm11 = 'media/green.jpg'
    alarm12 = 'media/green.jpg'
    alarm13 = 'media/green.jpg'


    number = [predict1, predict2, predict3, predict4, predict5, predict6, predict7, predict8, predict9, predict10, predict11, predict12, predict13]
    alarm = [alarm1, alarm2, alarm3, alarm4, alarm5, alarm6, alarm7, alarm8, alarm9, alarm10, alarm11, alarm12, alarm13]

    for i in range(len(number)):
        if number[i] < 80:
            alarm[i] = 'media/red.jpg'


    context = {
        "alarm1" : str(alarm1),
        "alarm2" : str(alarm2),
        "alarm3" : str(alarm3),
        "alarm4" : str(alarm4),
        "alarm5" : str(alarm5),
        "alarm6" : str(alarm6),
        "alarm7" : str(alarm7),
        "alarm8" : str(alarm8),
        "alarm9" : str(alarm9),
        "alarm10" : str(alarm10),
        "alarm11" : str(alarm11),
        "alarm12" : str(alarm12),
        "alarm13" : str(alarm13),

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
        "pengunjung_lidar" : str(pengunjung_lidar.value),

        "predict1" : str(predict1[0][0]),
        "predict2" : str(predict2[0][0]),
        "predict3" : str(predict3[0][0]),
        "predict4" : str(predict4[0][0]),
        "predict5" : str(predict5[0][0]),
        "predict6" : str(predict6[0][0]),
        "predict7" : str(predict7[0][0]),
        "predict8" : str(predict8[0][0]),
        "predict9" : str(predict9[0][0]),
        "predict10" : str(predict10[0][0]),
        "predict11" : str(predict11[0][0]),
        "predict12" : str(predict12[0][0]),
        "predict13" : str(predict13[0][0])
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
    
def on_message_ome(client, userdata, msg):
    susutelur_omega = Sensor.objects.get(name="susutelur_omega")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(susutelur_omega, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()

def on_message_sal(client, userdata, msg):
    susutelur_salmonella = Sensor.objects.get(name="susutelur_salmonella")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(susutelur_salmonella, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    

def on_message_mus(client, userdata, msg):
    dagingmerah_muscle = Sensor.objects.get(name="dagingmerah_muscle")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingmerah_muscle, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    
def on_message_dar(client, userdata, msg):
    dagingmerah_darah = Sensor.objects.get(name="dagingmerah_darah")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingmerah_darah, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()

def on_message_met(client, userdata, msg):
    dagingmerah_metana = Sensor.objects.get(name="dagingmerah_metana")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingmerah_metana, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
   

def on_message_eco(client, userdata, msg):
    dagingputih_ecoli = Sensor.objects.get(name="dagingputih_ecoli")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingputih_ecoli, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
   
def on_message_war(client, userdata, msg):
    dagingputih_warna = Sensor.objects.get(name="dagingputih_warna")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingputih_warna, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    
def on_message_amo(client, userdata, msg):
    dagingputih_amonia = Sensor.objects.get(name="dagingputih_amonia")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(dagingputih_amonia, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    


def on_message_vol(client, userdata, msg):
    karbohidrat_volume = Sensor.objects.get(name="karbohidrat_volume")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(karbohidrat_volume, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    
def on_message_kel(client, userdata, msg):
    karbohidrat_kelembaban = Sensor.objects.get(name="karbohidrat_kelembaban")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(karbohidrat_kelembaban, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
     
def on_message_oxy(client, userdata, msg):
    karbohidrat_oksigen = Sensor.objects.get(name="karbohidrat_oksigen")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(karbohidrat_oksigen, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
   

def on_message_ure(client, userdata, msg):
    sayuran_urea = Sensor.objects.get(name="sayuran_urea")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sayuran_urea, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    
def on_message_cah(client, userdata, msg):
    sayuran_cahaya = Sensor.objects.get(name="sayuran_cahaya")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sayuran_cahaya, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    
def on_message_tem(client, userdata, msg):
    sayuran_temperatur = Sensor.objects.get(name="sayuran_temperatur")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(sayuran_temperatur, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    

def on_message_pes(client, userdata, msg):
    buah_pestisida = Sensor.objects.get(name="buah_pestisida")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(buah_pestisida, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
   
def on_message_uku(client, userdata, msg):
    buah_ukuran = Sensor.objects.get(name="buah_ukuran")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(buah_ukuran, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
   
def on_message_ber(client, userdata, msg):
    buah_berat = Sensor.objects.get(name="buah_berat")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(buah_berat, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
   


def on_message_ang(client, userdata, msg):
    musim_angin = Sensor.objects.get(name="musim_angin")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(musim_angin, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    
def on_message_lis(client, userdata, msg):
    musim_listrik = Sensor.objects.get(name="musim_listrik")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(musim_listrik, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
     
def on_message_bar(client, userdata, msg):
    musim_barometer = Sensor.objects.get(name="musim_barometer")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(musim_barometer, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    

def on_message_cod(client, userdata, msg):
    penjualan_barcode = Sensor.objects.get(name="penjualan_barcode")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(penjualan_barcode, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    
def on_message_cas(client, userdata, msg):
    penjualan_cashflow = Sensor.objects.get(name="penjualan_cashflow")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(penjualan_cashflow, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    
def on_message_inf(client, userdata, msg):
    penjualan_infrared = Sensor.objects.get(name="penjualan_infrared")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(penjualan_infrared, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    

def on_message_ult(client, userdata, msg):
    pengunjung_ultrasonic = Sensor.objects.get(name="pengunjung_ultrasonic")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(pengunjung_ultrasonic, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    
def on_message_kam(client, userdata, msg):
    pengunjung_kamera = Sensor.objects.get(name="pengunjung_kamera")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(pengunjung_kamera, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    
def on_message_lid(client, userdata, msg):
    pengunjung_lidar = Sensor.objects.get(name="pengunjung_lidar")
    data = {
        'value': msg.payload.decode('utf-8')
    }
    serializer = SensorSerializer(pengunjung_lidar, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
    



client = mqtt.Client("sensor")

client.message_callback_add('susutelur/protein', on_message_pro)
client.message_callback_add('susutelur/omega', on_message_ome)
client.message_callback_add('susutelur/salmonella', on_message_sal)

client.message_callback_add('dagingmerah/muscle', on_message_mus)
client.message_callback_add('dagingmerah/darah', on_message_dar)
client.message_callback_add('dagingmerah/metana', on_message_met)

client.message_callback_add('dagingputih/ecoli', on_message_eco)
client.message_callback_add('dagingputih/warna', on_message_war)
client.message_callback_add('dagingputih/amonia', on_message_amo)


client.message_callback_add('karbohidrat/volume', on_message_vol)
client.message_callback_add('karbohidrat/kelembaban', on_message_kel)
client.message_callback_add('karbohidrat/oksigen', on_message_oxy)

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