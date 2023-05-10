import pandas as pd
import numpy as np
from sklearn import linear_model
from csv import writer
from django.conf import settings

class BaseLinearRegression:
    def __init__(self,training_data):
        self.df = pd.read_csv(settings.ML_ROOT + training_data)
        self.model = linear_model.LinearRegression()
        self.model.fit(self.df.iloc[:, 0:3], self.df.iloc[:,-1:])
        
    def predict(self, value):
        return self.model.predict([value])


ml_susutelur = BaseLinearRegression('dairy.csv')
ml_dagingmerah = BaseLinearRegression('redmeat.csv')
ml_dagingputih = BaseLinearRegression('whitemeat.csv')

ml_karbohidrat = BaseLinearRegression('grain.csv')
ml_sayuran = BaseLinearRegression('vegetable.csv')
ml_buah = BaseLinearRegression('fruit.csv')

ml_musim = BaseLinearRegression('weather.csv')
ml_penjualan = BaseLinearRegression('sales.csv')
ml_pengunjung = BaseLinearRegression('customer.csv')


ml_perawatan = BaseLinearRegression('care.csv')
ml_panen = BaseLinearRegression('harvest.csv')
ml_promosi = BaseLinearRegression('promotion.csv')


ml_keuntungan = BaseLinearRegression('profit.csv')

# with open('smartfarm.csv', 'a') as f_object:
#     writer_object = writer(f_object)
#     writer_object.writerow(list_farm)
#     f_object.close()

# with open('smartplant.csv', 'a') as f_object:
#     writer_object = writer(f_object)
#     writer_object.writerow(list_plant)
#     f_object.close()

# with open('smartresto.csv', 'a') as f_object:
#     writer_object = writer(f_object)
#     writer_object.writerow(list_resto)
#     f_object.close()

# def write_system(system_name):
#     with open('smart' + system_name + '.csv', 'a') as f_object:
#         writer_object = writer(f_object)
#         writer_object.writerow(list_resto)
#         f_object.close()