# -*- coding: utf-8 -*-
"""
Modificado el 22 de septiembre de 2024

@author: user
"""

import numpy as np
import scipy.stats as stats
from datetime import datetime

# Función para calcular el precio de una opción Call usando el modelo Black-Scholes
def calcular_precio_opcion_call(S_actual, strike_price, tiempo_expiracion, tasa_riesgo, volatilidad):
    # Cálculo intermedio de los parámetros d1 y d2
    d1 = (np.log(S_actual / strike_price) + (tasa_riesgo + 0.5 * volatilidad ** 2) * tiempo_expiracion) / (volatilidad * np.sqrt(tiempo_expiracion))
    d2 = d1 - volatilidad * np.sqrt(tiempo_expiracion)
    
    # Cálculo del precio de la opción Call
    precio_call = S_actual * stats.norm.cdf(d1) - strike_price * np.exp(-tasa_riesgo * tiempo_expiracion) * stats.norm.cdf(d2)
    return precio_call

# Parámetros iniciales
precio_subyacente = 435.27
precio_ejercicio = 370
tasa_libre_riesgo = 0.0476
volatilidad_implicita = 1.2

# Cálculo del tiempo en años hasta la expiración de la opción
hoy = datetime.now()
fecha_expiracion_opcion = datetime(2024, 9, 27)
tiempo_restante = (fecha_expiracion_opcion - hoy).days / 365.0

# Cálculo del precio usando la función de Black-Scholes
precio_call_black_scholes = calcular_precio_opcion_call(precio_subyacente, precio_ejercicio, tiempo_restante, tasa_libre_riesgo, volatilidad_implicita)

# Imprimir resultado
print(f"El precio calculado para la opción Call es: {precio_call_black_scholes:.2f}")