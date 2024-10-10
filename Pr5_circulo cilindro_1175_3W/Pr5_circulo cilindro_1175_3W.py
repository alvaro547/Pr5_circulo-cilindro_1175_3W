print(" ")
print("Alvaro Campechano 3W")
print(" ")
import math

def calcular_area_y_volumen_circulo(radio):
    """
    Calcula el área de un círculo y el volumen de una esfera.
    
    Args:
    radio (float): El radio del círculo/esfera.
    
    Returns:
    tuple: (área del círculo, volumen de la esfera)
    """
    # Calcular el área del círculo
    area = math.pi * (radio ** 2)
    
    # Calcular el volumen de la esfera
    volumen = (4/3) * math.pi * (radio ** 3)
    
    return area, volumen

def calcular_volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro utilizando la función de área y volumen de un círculo.
    
    Args:
    radio (float): El radio de la base del cilindro.
    altura (float): La altura del cilindro.
    
    Returns:
    float: Volumen del cilindro.
    """
    # Calcular el área de la base del cilindro (círculo)
    area_base, _ = calcular_area_y_volumen_circulo(radio)
    
    # Calcular el volumen del cilindro
    volumen_cilindro = area_base * altura
    
    return volumen_cilindro

# Ejemplo de uso
radio = 5  # Cambia este valor según sea necesario
altura = 10  # Cambia este valor según sea necesario

# Calcular área y volumen de la esfera
area_circulo, volumen_esfera = calcular_area_y_volumen_circulo(radio)
print(f"Área del círculo: {area_circulo:.2f}")
print(f"Volumen de la esfera: {volumen_esfera:.2f}")

# Calcular volumen del cilindro
volumen_cilindro = calcular_volumen_cilindro(radio, altura)
print(f"Volumen del cilindro: {volumen_cilindro:.2f}")
