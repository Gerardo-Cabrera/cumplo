from django.db import models
from decimal import Decimal
import requests
import configparser
import os


class Consulta(models.Model):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), '../conf', 'config.cfg'))

    def obtenerInformacion(self, data):
        serie_udis = self.config['datos']['serie_udis']
        serie_udis = serie_udis.replace("'", "")
        serie_tipo_cambio = self.config['datos']['serie_tipo_cambio']
        serie_tipo_cambio = serie_tipo_cambio.replace("'", "")
        token = self.config['datos']['token']
        token = token.replace("'", "")
        fecha_inicial = data['fechaInicial']
        fecha_final = data['fechaFinal']
        data_udis = requests.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/'+ serie_udis +'/datos/'+ fecha_inicial +'/'+ fecha_final +'?token='+ token)
        datos_udis = data_udis.json()
        datos_udis = datos_udis['bmx']['series'][0]
        datos_udis = self.valores(datos_udis)
        valores_udis = {'minimo': datos_udis['minimo'], 'maximo': datos_udis['maximo'], 'promedio': datos_udis['promedio']}
        data_tipo_cambio = requests.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/'+ serie_tipo_cambio +'/datos/'+ fecha_inicial +'/'+ fecha_final +'?token='+ token)
        datos_tipo_cambio = data_tipo_cambio.json()
        datos_tipo_cambio = datos_tipo_cambio['bmx']['series'][0]
        datos_tipo_cambio = self.valores(datos_tipo_cambio)
        valores_cambios = {'minimo': datos_tipo_cambio['minimo'], 'maximo': datos_tipo_cambio['maximo'], 'promedio': datos_tipo_cambio['promedio']}
        datos_respuesta = {
                            'datos_udis': datos_udis['datos'], 
                            'datos_tipo_cambio': datos_tipo_cambio['datos'],
                            'valores_udis': valores_udis,
                            'valores_cambios': valores_cambios
                          }
        return datos_respuesta

    def valores(self, data):
        lista_valores_udis = []

        for dato in data['datos']:
            dato['dato'] = Decimal(dato['dato'])
            dato['dato'] = round(dato['dato'], 3)
            lista_valores_udis.append(dato['dato'])
        
        minimo = min(lista_valores_udis)
        maximo = max(lista_valores_udis)
        cantidad_elementos = len(lista_valores_udis)
        promedio = sum(lista_valores_udis) / cantidad_elementos
        promedio = round(promedio, 3)
        data['minimo'] = minimo
        data['maximo'] = maximo
        data['promedio'] = promedio
        return data
