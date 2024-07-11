
from gpiozero import RGBLED
import time

# Crear el objeto RGBLED
rgb_led = RGBLED(rojo=19, verde=26, azul=13)

while True:
    # Encender el LED rojo
    rgb_led.rojo = 1
    time.sleep(1)
    rgb_led.rojo = 0

    # Encender el LED azul
    rgb_led.azul = 1
    time.sleep(0.5)
    rgb_led.azul = 0

    # Encender el LED verde
    rgb_led.verde = 1
    time.sleep(0.25)
    rgb_led.verde = 0
